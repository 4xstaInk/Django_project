# Generated by Django 3.2.5 on 2021-07-18 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210717_2035'),
        ('tutors', '0004_auto_20210717_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='students.field'),
        ),
    ]
