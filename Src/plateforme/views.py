from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Worker, Employeur
from .forms import CustomUserCreationForm, WorkerForm, EmployeurForm


def bienvenue(request):
    return render(request, 'plateforme/bienvenue.html')

def hello_world(request):
    return HttpResponse("Hello World")


def register_worker(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            worker_form = WorkerForm(request.POST, instance=Worker(user=user))
            if worker_form.is_valid():
                worker_form.save()

            if user_form.cleaned_data.get('user_type') == 'worker':
                worker_form = WorkerForm(request.POST, instance=Worker(user=user))
                if worker_form.is_valid():
                    worker_form.save()

            return redirect('bienvenue')

    else:
        user_form = CustomUserCreationForm()
        worker_form = WorkerForm()

    return render(request, 'plateforme/inscriptionuser.html', {'user_form': user_form, 'worker_form': worker_form})


def RegisterEmployeur(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            employer_form = EmployeurForm(request.POST, instance=Employeur(user=user))
            if employer_form.is_valid():
                employer_form.save()

            return redirect('bienvenue')

    else:
        user_form = CustomUserCreationForm()
        employer_form = EmployeurForm()

    return render(request, 'plateforme/inscription.html', {'user_form': user_form, 'employer_form': employer_form})


from django.contrib.auth import authenticate, login as auth_login

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
