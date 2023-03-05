from django.contrib import admin
from .models import CustomUser, InterimUser, Utilisateur
#, Employeur, Worker


admin.site.register(InterimUser)
admin.site.register(CustomUser)
admin.site.register(Utilisateur)