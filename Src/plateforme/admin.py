from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Interim, Employeur

admin.site.register(Interim)
admin.site.register(Employeur)