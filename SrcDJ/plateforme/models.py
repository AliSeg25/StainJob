from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.widgets import PasswordInput
from django.contrib.auth.hashers import make_password


class Interim(models.Model):

    phone_number = models.CharField(max_length=20)
    skills = models.CharField(max_length=255)
    availability =  models.CharField(max_length=255)

    # inclure les champs par défaut d'AbstractUser
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128)

    # La fonction make_password de Django permet de hacher les mots de passe avant de les stocker en base de données
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.username

class Employeur(models.Model):

    company_name = models.CharField(max_length=255)

    # inclure les champs par défaut d'AbstractUser
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128)

    # La fonction make_password de Django permet de hacher les mots de passe avant de les stocker en base de données
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name