# Generated by Django 3.2.5 on 2021-07-18 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210717_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='field',
            new_name='fields',
        ),
    ]