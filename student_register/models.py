from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=50)

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    stu_code = models.CharField(max_length=10)
    batch = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)