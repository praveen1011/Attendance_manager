from django.db import models
from django.contrib import admin

# Create your models here.
class logins(models.Model):
    faculty_id = models.CharField(max_length=200,primary_key=True)
    faculty_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
class registered(models.Model):
    subject_name = models.CharField(max_length=200,unique=False,null=False)
    subject_code = models.CharField(max_length=200,primary_key=True)
    faculty_name = models.CharField(max_length=200,null=False)
    faculty_id = models.CharField(max_length=200,null=False)