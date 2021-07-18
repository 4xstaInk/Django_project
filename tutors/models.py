from django.db import models


# Create your models here.
class Tutor(models.Model):
    fullname = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    sex = models.CharField(max_length=70, blank=False, default='')
    field = models.CharField(max_length=70, blank=True, null=True)
    courses = models.CharField(max_length=70, blank=False, default='')
    age = models.CharField(max_length=70, blank=False, default='')
    marital_status = models.CharField(max_length=70, blank=False, default='')
    nationality = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.fullname