from django.urls import path
from . import views
#urls.py


urlpatterns = [
    path('bienvenue/', views.bienvenue, name='bienvenue'),
    path('hello/', views.hello_world, name='hello_world'),
    path('inscriptionuser/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]
