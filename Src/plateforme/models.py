from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    skills = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

class Worker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    max_distance = models.IntegerField(blank=True, null=True)

class Employeur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()