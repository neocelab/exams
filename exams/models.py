from django.db import models
from django.contrib.auth.models import User

class TestPaper(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

class Exam(models.Model):
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE)
    virtual_examinee_id = models.CharField(max_length=100)
    examinee = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

class VirtualUser(models.Model):
    virtual_user_id = models.CharField(max_length=100)
    examinee = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField()