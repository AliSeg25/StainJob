from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    pass


class InterimUser(Utilisateur):
    prenom = models.CharField(max_length=30, blank=True)
    nom = models.CharField(max_length=30, blank=True)
    distance_max = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Distance maximale de déplacement")
    adresse = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.utilisateur.username

class EmpUser(Utilisateur):
    societe = models.CharField(max_length=30, blank=True)
    nom = models.CharField(max_length=30, blank=True)
    adresse = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.EmpUser.societe
