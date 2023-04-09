from django.utils import timezone

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TestPaper, Exam, VirtualUser
from .forms import ExamForm
from datetime import date, timedelta
import random
from datetime import datetime

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

        virtual_user_list = VirtualUser.objects.filter(create_date__range=[create_date - timedelta(days=0), create_date]).all()

    context = {'virtual_user_list': virtual_user_list}
    return render(request, 'exams/virtual_user_list.html', context)


def test_paper_list(request):
    test_paper_list = TestPaper.objects.order_by('-create_date')
    context = {'test_paper_list': test_paper_list}
    return render(request, 'exams/test_paper_list.html', context)

@login_required(login_url='common:login')
def record(request, test_paper_id):
    test_paper = get_object_or_404(TestPaper, pk=test_paper_id)
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.test_paper = test_paper
            virtual_user_id = form.cleaned_data.get("virtual_examinee_id")
            virtual_user = get_object_or_404(VirtualUser, virtual_user_id=virtual_user_id, create_date=date.today())
            exam.examinee = virtual_user.examinee
            exam.create_date = timezone.now()
            exam.save()
            return redirect('exams:exam_list')
        else:
            context = {'test_paper':test_paper, 'form': form}
            return render(request, 'exams/record.html', context)
    else:
        form = ExamForm()
    context = {'test_paper':test_paper, 'form': form}
    return render(request, 'exams/record.html', context)

def exam_list(request):
    exams = Exam.objects.order_by('-test_paper__create_date', '-create_date')
    context = {'exam_list': exams}
    return render(request, 'exams/exam_list.html', context)