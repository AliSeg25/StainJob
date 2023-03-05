from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Employeur, Worker

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    skills = forms.CharField(max_length=100, required=False)
    experience = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'password1', 'password2', 'skills', 'experience', 'location')


class WorkerForm(forms.ModelForm):
    max_distance = forms.IntegerField()

    class Meta:
        model = Worker
        fields = ('max_distance',)


class EmployeurForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = Employeur
        fields = ('company_name', 'email',)









class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
