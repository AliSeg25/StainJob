from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InterimUser, EmpUser





#Formulaire pour cree un Interim
class InterimUserForm(UserCreationForm):

    class Meta:
        model = InterimUser
        fields = ('username', 'prenom', 'nom', 'email', 'password1', 'password2', 'telephone', 'adresse', 'distance_max')



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