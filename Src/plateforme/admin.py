from django.contrib import admin
from .models import CustomUser, Employeur, Worker

admin.site.register(CustomUser)
admin.site.register(Employeur)
admin.site.register(Worker)