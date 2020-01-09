from django.dispatch import receiver
from .signals import *
from django.forms import CharField, ValidationError

@receiver(user_activated)
def set_registration_bonuses(sender, instance, **kwargs):
    inviter = instance.profile.inviter #user inviter
    prize = inviter.referals.count() + 1

    inviter.profile.points += prize
    inviter.profile.save()
