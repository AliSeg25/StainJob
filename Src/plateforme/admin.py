from django.contrib import admin
from .models import EmpUser, InterimUser, Utilisateur
#, Employeur, Worker


admin.site.register(InterimUser)
admin.site.register(EmpUser)
admin.site.register(Utilisateur)