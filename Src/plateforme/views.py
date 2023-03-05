from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate



def bienvenue(request):
    return render(request, 'plateforme/bienvenue.html')

def hello_world(request):
    return HttpResponse("Hello World")

from .forms import InterimUserForm

def register_worker(request):
    if request.method == 'POST':
        form = InterimUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a été créé, {username}!')
            return redirect('bienvenue')
    else:
        form = InterimUserForm()
    return render(request, 'plateforme/inscriptionuser.html', {'form': form})




from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username:', username)
        print('password:', password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('bienvenue')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'plateforme/login.html')





from .forms import CustomUserCreationForm

def create_employeur(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employeur = True
            user.save()
            return redirect('bienvenue')
    else:
        form = CustomUserCreationForm()
    return render(request, 'plateforme/inscription.html', {'form': form})