from django.urls import path
from . import views
#urls.py


urlpatterns = [
    path('bienvenue/', views.bienvenue, name='bienvenue'),
    path('inscription/', views.RegisterEmployeur, name='hello_world'),
    path('inscriptionuser/', views.register_worker, name='signup'),
    path('login/', views.login_view, name='login'),
]
