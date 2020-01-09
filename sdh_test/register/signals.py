from django.db.models.signals import post_save
from django.dispatch import Signal

from django.contrib.auth.models import User
from .models import Profile

# Create your signals here.


def createProfileForUser(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(createProfileForUser, sender=User, weak=False)

user_activated = Signal()
