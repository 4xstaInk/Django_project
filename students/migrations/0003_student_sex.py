# Generated by Django 3.2.5 on 2021-07-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_students_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(default='', max_length=70),
        ),
    ]
