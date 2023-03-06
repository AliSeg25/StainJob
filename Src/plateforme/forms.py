from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InterimUser

class InterimUserForm(UserCreationForm):

    class Meta:
        model = InterimUser
        fields = ('username', 'prenom', 'nom', 'email', 'password1', 'password2', 'telephone', 'adresse', 'distance_max')


from .models import EmpUser

class EmpUserForm(UserCreationForm):

    class Meta:
        model = EmpUser
        fields = ['username', 'email', 'password1', 'password2', 'societe', 'nom', 'adresse', 'telephone', 'domaine']