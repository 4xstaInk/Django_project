from django.db import models
from tutors.models import Tutor

# Create your models here.
class Student(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    fullname = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    sex = models.CharField(max_length=70, blank=False, default='')
    field = models.CharField(max_length=70, blank=False, default='')
    student_id_number = models.CharField(max_length=70, blank=False, default='')
    year_enrolled = models.CharField(max_length=70, blank=False, default='')
    age = models.CharField(max_length=70, blank=False, default='')
    marital_status = models.CharField(max_length=70, blank=False, default='')
    nationality = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    tutors = models.ManyToMany(to=Tutor, blank=True)