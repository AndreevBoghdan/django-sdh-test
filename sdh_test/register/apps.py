from django.apps import AppConfig
from django.contrib import admin
from .models import Profile

class RegistrationConfig(AppConfig):
    name = 'registration'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)