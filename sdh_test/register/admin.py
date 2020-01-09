from django.contrib import admin

# Register your models here.

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'invitation_code', 'inviter', 'points']


admin.site.register(Profile, ProfileAdmin)
