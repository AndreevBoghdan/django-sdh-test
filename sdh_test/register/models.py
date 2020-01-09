from django.db import models

# Create your models here.

from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE)
    inviter = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null = True,
        related_name="inviter")
    invitation_code = models.CharField(
    	max_length=128,
    	default = '')


    def __str__(self):
        return '{} profile'.format(self.user.username)
