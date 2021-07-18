from django.db import models


# Create your models here.
class Tutor(models.Model):
    fullname = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    sex = models.CharField(max_length=70, blank=False, default='')
    field = models.ForeignKey(to="students.Field", blank=True, null=True,
                              on_delete=models.DO_NOTHING)
    courses = models.CharField(max_length=70, blank=False, default='')
    age = models.CharField(max_length=70, blank=False, default='')
    marital_status = models.CharField(max_length=70, blank=False, default='')
    nationality = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.fullname