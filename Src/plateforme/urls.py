from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#urls.py


urlpatterns = [
    path('bienvenue/', views.bienvenue, name='bienvenue'),
    path('inscription_emp/', views.create_employeur, name='hello_world'),
    path('inscriptionuser_worker/', views.register_worker, name='signup'),
    path('login/', views.login_view, name='login'),
    path('compte/', views.compte, name='compte'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('modifier_compte/', views.update_account, name='update_account'),
]
