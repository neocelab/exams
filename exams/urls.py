from django.urls import path

from . import views

app_name = 'exams'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('virtual_usrs/', views.virtual_user_list, name='virtual_user_list'),
    path('test_papers/', views.test_paper_list, name='test_paper_list'),
    path('record/<int:test_paper_id>/', views.record, name='exam_record'),
    path('exams/', views.exam_list, name='exam_list'),
]

