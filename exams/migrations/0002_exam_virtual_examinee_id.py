# Generated by Django 4.0.3 on 2023-04-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='virtual_examinee_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
