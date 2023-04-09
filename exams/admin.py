from django.contrib import admin
from .models import TestPaper, Exam, VirtualUser

class TestPaperAdmin(admin.ModelAdmin):
    search_fields = ['id']

class EaxmAdmin(admin.ModelAdmin):
    search_fields = ['id']

class VirtualUserAdmin(admin.ModelAdmin):
    search_fields = ['id']

admin.site.register(TestPaper, TestPaperAdmin)
admin.site.register(Exam, EaxmAdmin)
admin.site.register(VirtualUser, VirtualUserAdmin)
