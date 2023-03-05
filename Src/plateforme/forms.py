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


from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    ville = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'ville']