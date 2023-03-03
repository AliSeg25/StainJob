from django import forms
from .models import Interim
from .models import Employeur


class InterimForm(forms.ModelForm):
    class Meta:
        # La class Meta contient les informations sur le models lier au formulaire
        model = Interim
        # Les champs doivent etre afficher ici
        fields = ['phone_number', 'skills', 'availability', 'username', 'first_name', 'last_name', 'email', 'password']
        # pou cacher le Mdp
        widgets = {'password': forms.PasswordInput()}


class EmployeurForm(forms.ModelForm):
    class Meta:
        # La class Meta contient les informations sur le models lier au formulaire
        model = Employeur
        # Les champs doivent etre afficher ici
        fields = ['company_name', 'username', 'first_name', 'last_name', 'email', 'password']
        # pou cacher le Mdp
        widgets = {'password': forms.PasswordInput()}

