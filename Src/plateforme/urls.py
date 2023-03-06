from django.urls import path
from . import views
#urls.py


urlpatterns = [
    path('bienvenue/', views.bienvenue, name='bienvenue'),
    path('inscription_emp/', views.create_employeur, name='hello_world'),
    path('inscriptionuser_worker/', views.register_worker, name='signup'),
    path('login/', views.login_view, name='login'),
]
