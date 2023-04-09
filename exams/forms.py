from django import forms
from exams.models import Exam

class ExamForm(forms.ModelForm):
    virtual_examinee_id = forms.CharField(max_length=10, label="가상 시험자 번호")

    class Meta:
        model = Exam # 사용할 모델
        fields = ['virtual_examinee_id', 'score'] # ExamForm 사용할 Exam 모델의 속성
        labels = {
            'virtual_examinee_id': '가상 시험자 번호',
            'score': '얻은 점 수',
        }