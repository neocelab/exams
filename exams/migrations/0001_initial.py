# Generated by Django 4.0.3 on 2023-04-03 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('examinee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('test_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.testpaper')),
            ],
        ),
    ]