from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TestPaper, Exam, VirtualUser
from .forms import ExamForm
from datetime import date, timedelta, datetime

import random


def menu(request):
    return render(request, 'exams/menu.html')

@login_required(login_url='common:login')
def virtual_user_list(request):
    create_date = date.today()
    virtual_user_list = VirtualUser.objects.filter(create_date__range=[create_date - timedelta(days=0), create_date]).all()
    if virtual_user_list.count()==0:
        print('발생')
        users = User.objects.filter(is_active=True, is_staff=False, is_superuser=False).all()
        v_ids = list(range(1, users.count()+1))
        random.shuffle(v_ids)
        for idx, user in enumerate(users):
            virtual_user = VirtualUser(virtual_user_id=v_ids[idx], examinee=user, create_date=create_date )
            virtual_user.save()

    virtual_user_list = VirtualUser.objects.order_by('-create_date')

    context = {'virtual_user_list': virtual_user_list}
    return render(request, 'exams/virtual_user_list.html', context)

def test_paper_list(request):
    test_paper_list = TestPaper.objects.order_by('-create_date')
    context = {'test_paper_list': test_paper_list, 'today': timezone.now().date()}
    return render(request, 'exams/test_paper_list.html', context)

@login_required(login_url='common:login')
def record(request, test_paper_id):
    test_paper = get_object_or_404(TestPaper, pk=test_paper_id)
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            virtual_user_id = form.cleaned_data.get("virtual_examinee_id")
            virtual_user_list = VirtualUser.objects.filter(virtual_user_id=virtual_user_id, create_date=timezone.now().date()).all()
            if virtual_user_list.count() == 0: #만약 존재하지 않은 가상 시험자 번호이면
                form.add_error('virtual_examinee_id', "오늘 날자에 존재하지 않는 가상 시험자 번호입니다.")

            else:#만약 존재하는 가상 시험자 번호이면 신규 기록 또는 변경한다.
                exam_list = Exam.objects.filter(test_paper_id=test_paper_id, virtual_examinee_id=virtual_user_id)
                if exam_list.count() > 0: #이미 기록되었다면 변경을 한다.
                    form = ExamForm(request.POST, instance=exam_list[0])
                    exam = form.save(commit=False)
                    exam.modify_date = timezone.now()
                else:
                    exam = form.save(commit=False)
                    exam.test_paper = test_paper

                    exam.examinee = virtual_user_list[0].examinee
                    exam.create_date = timezone.now()
                exam.save()
                return redirect('exams:exam_list')

        #입력 사항이 유효하지 않으면 에러 및 이미 입력된 것들은 다시 출력하고 다시 입력을 기다린다.
        context = {'test_paper':test_paper, 'form': form}
        return render(request, 'exams/record.html', context)
    else: # 입력 준비 요청 시
        form = ExamForm()
    context = {'test_paper':test_paper, 'form': form}
    return render(request, 'exams/record.html', context)

def exam_list(request):
    exams = Exam.objects.order_by('-test_paper__create_date', '-create_date')
    context = {'exam_list': exams}
    return render(request, 'exams/exam_list.html', context)