# Generated by Django 3.2.5 on 2021-07-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('sex', models.CharField(default='', max_length=70)),
                ('field', models.CharField(default='', max_length=70)),
                ('courses', models.CharField(default='', max_length=70)),
                ('age', models.CharField(default='', max_length=70)),
                ('marital_status', models.CharField(default='', max_length=70)),
                ('nationality', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
