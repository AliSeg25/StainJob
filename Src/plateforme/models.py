from django.db import models
from django.contrib.auth.models import AbstractUser


#fichier models.py
class Utilisateur(AbstractUser):
    pass


class InterimUser(Utilisateur):
    prenom = models.CharField(max_length=30, blank=True)
    nom = models.CharField(max_length=30, blank=True)
    distance_max = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Distance maximale de déplacement")
    adresse = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=20, blank=True)


    lundi_dispo = models.BooleanField(default=False)
    lundi_debut = models.TimeField(null=True, blank=True)
    lundi_fin = models.TimeField(null=True, blank=True)
    mardi_dispo = models.BooleanField(default=False)
    mardi_debut = models.TimeField(null=True, blank=True)
    mardi_fin = models.TimeField(null=True, blank=True)
    mercredi_dispo = models.BooleanField(default=False)
    mercredi_debut = models.TimeField(null=True, blank=True)
    mercredi_fin = models.TimeField(null=True, blank=True)
    jeudi_dispo = models.BooleanField(default=False)
    jeudi_debut = models.TimeField(null=True, blank=True)
    jeudi_fin = models.TimeField(null=True, blank=True)
    vendredi_dispo = models.BooleanField(default=False)
    vendredi_debut = models.TimeField(null=True, blank=True)
    vendredi_fin = models.TimeField(null=True, blank=True)
    samedi_dispo = models.BooleanField(default=False)
    samedi_debut = models.TimeField(null=True, blank=True)
    samedi_fin = models.TimeField(null=True, blank=True)
    dimanche_dispo = models.BooleanField(default=False)
    dimanche_debut = models.TimeField(null=True, blank=True)
    dimanche_fin = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.username






class EmpUser(Utilisateur):
    societe = models.CharField(max_length=30, blank=True)
    nom = models.CharField(max_length=30, blank=True)
    adresse = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    domaine = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.societe
