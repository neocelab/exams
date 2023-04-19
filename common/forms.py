from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    first_name = forms.CharField(max_length=10, label="성")
    last_name = forms.CharField(max_length=10, label="이름")
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")
        labels = {
            'username': 'ID'
        }