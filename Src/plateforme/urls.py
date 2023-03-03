from django.urls import path
from . import views
#urls.py


urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('inscription/', views.InscrptionInterim, name='inscription'),
    path('incription_employeur/', views.InscrptionEmployeur, name='incription_employeur'),
    path('login/', views.login_view, name='login'),
]
