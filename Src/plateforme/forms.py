from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InterimUser, EmpUser

# fichier formulaire forms.py



#Formulaire pour cree un Interim
class InterimUserForm(UserCreationForm):

    class Meta:
        model = InterimUser
        fields = ('username', 'prenom', 'nom', 'email', 'password1', 'password2', 'telephone', 'adresse', 'distance_max')


class DisponibiliteForm(forms.ModelForm):
    class Meta:
        model = InterimUser
        fields = [
            'lundi_dispo',
            'lundi_debut',
            'lundi_fin',
            'mardi_dispo',
            'mardi_debut',
            'mardi_fin',
            'mercredi_dispo',
            'mercredi_debut',
            'mercredi_fin',
            'jeudi_dispo',
            'jeudi_debut',
            'jeudi_fin',
            'vendredi_dispo',
            'vendredi_debut',
            'vendredi_fin',
            'samedi_dispo',
            'samedi_debut',
            'samedi_fin',
            'dimanche_dispo',
            'dimanche_debut',
            'dimanche_fin',
        ]
        widgets = {
            'lundi_debut': forms.TimeInput(format='%H:%M'),
            'lundi_fin': forms.TimeInput(format='%H:%M'),
            'mardi_debut': forms.TimeInput(format='%H:%M'),
            'mardi_fin': forms.TimeInput(format='%H:%M'),
            'mercredi_debut': forms.TimeInput(format='%H:%M'),
            'mercredi_fin': forms.TimeInput(format='%H:%M'),
            'jeudi_debut': forms.TimeInput(format='%H:%M'),
            'jeudi_fin': forms.TimeInput(format='%H:%M'),
            'vendredi_debut': forms.TimeInput(format='%H:%M'),
            'vendredi_fin': forms.TimeInput(format='%H:%M'),
            'samedi_debut': forms.TimeInput(format='%H:%M'),
            'samedi_fin': forms.TimeInput(format='%H:%M'),
            'dimanche_debut': forms.TimeInput(format='%H:%M'),
            'dimanche_fin': forms.TimeInput(format='%H:%M'),
        }

#Formulaire pour cree un Employer
class EmpUserForm(UserCreationForm):

    class Meta:
        model = EmpUser
        fields = ['username', 'email', 'password1', 'password2', 'societe', 'nom', 'adresse', 'telephone', 'domaine']


#Pour changer les information d'un interim
class InterimUserUpdateForm(forms.ModelForm):
    class Meta:
        model = InterimUser
        fields = ['prenom', 'nom', 'email', 'telephone', 'adresse', 'distance_max']


#Pour changer les information d'un Emp
class EmpUserUpdateForm(forms.ModelForm):
    class Meta:
        model = EmpUser
        fields = ['societe', 'nom', 'email', 'telephone', 'adresse', 'domaine']