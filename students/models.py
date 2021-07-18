from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    fullname = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    sex = models.CharField(max_length=70, blank=False, default='')
    fields = models.ManyToManyField(to=Field, blank=True)
    student_id_number = models.CharField(max_length=70, blank=False, default='')
    year_enrolled = models.CharField(max_length=70, blank=False, default='')
    age = models.CharField(max_length=70, blank=False, default='')
    marital_status = models.CharField(max_length=70, blank=False, default='')
    nationality = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')

    def __str__(self):
        return self.fullname