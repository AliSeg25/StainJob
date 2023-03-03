from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import InterimForm
from .forms import EmployeurForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



def hello_world(request):
    return HttpResponse("Hello World")

def InscrptionInterim(request):
    # Affichier un formulaire vide
    form = InterimForm()
    if request.method == 'POST':
        # cree une instance du formulaire
        form = InterimForm(request.POST)
        # verification si formulaire valide
        if form.is_valid():
            interim = form.save()
            messages.success(request, 'Inscription réussie')
            return redirect('hello_world')
        else:
            messages.error(request, 'Une erreur est survenue. Veuillez corriger les erreurs ci-dessous.')
    else:
        return render(request, 'plateforme/inscription.html', {'form': form})

def InscrptionEmployeur(request):
    # affichier le formulaire
    form = EmployeurForm()
    #verification de la requet
    if request.method == 'POST':
        # cree une instance du formulaire
        form = EmployeurForm(request.POST)
        # Verification
        if form.is_valid():
            employeur = form.save()
            messages.success(request, 'Inscription réussie')
            return redirect('hello_world')
        else:messages.error(request, 'Une erreur est survenue. Veuillez corriger les erreurs ci-dessous.')
    return render(request, 'plateforme/inscription.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hello_world')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'plateforme/login.html', {'form': form})

