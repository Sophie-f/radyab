from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=256)
    f_name = models.CharField(max_length=512)
    age = models.IntegerField(default=25, null=True)
    gender = models.BooleanField(default=True)
    lesson = models.ManyToManyField('Lesson')
    student_class = models.ForeignKey('StudentClass', on_delete=models.CASCADE, null=True)


class StudentClass(models.Model):
    name = models.CharField(max_length=64)


class Lesson(models.Model):
    name = models.CharField(max_length=256)


class Income(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    income = models.IntegerField(default=0)
    mounthly_income = models.IntegerField(default=0)

