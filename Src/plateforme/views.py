from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import InterimUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InterimUserForm, InterimUserUpdateForm


def bienvenue(request):
    return render(request, 'plateforme/bienvenue.html')

@login_required
def compte(request):
    utilisateur = request.user.interimuser
    return render(request, 'plateforme/compte.html', {'utilisateur': utilisateur})

@login_required
def update_account(request):
    user = request.user.interimuser
    if request.method == 'POST':
        form = InterimUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vos informations ont été mises à jour.')
            return redirect('compte')
    else:
        form = InterimUserUpdateForm(instance=user)
    return render(request, 'plateforme/modifier_compte.html', {'form': form})

#Creation de compte interim
def register_worker(request):
    if request.method == 'POST':
        form = InterimUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenue')
    else:
        form = InterimUserForm()
    return render(request, 'plateforme/inscription_worker.html', {'form': form})



# creation de compte Utilisateur
from .forms import EmpUserForm

def create_employeur(request):
    if request.method == 'POST':
        form = EmpUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenue')
    else:
        form = EmpUserForm()
    return render(request, 'plateforme/inscription_emp.html', {'form': form})


#Connexion a un utilisateur
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('compte')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'plateforme/login.html')
