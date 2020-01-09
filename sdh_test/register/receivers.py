from django.dispatch import receiver
from .signals import *  # noqa


@receiver(user_activated)
def set_registration_bonuses(sender, instance, **kwargs):
    inviter = instance.profile.inviter  # user inviter
    if inviter is not None:
        prize = inviter.referals.count() + 1
        while inviter is not None and prize > 0:
            next_inviter = inviter.profile.inviter
            if next_inviter is not None:
                inviter.profile.points += 1
                inviter.profile.save()
                inviter = next_inviter
                prize -= 1
            else:
                inviter.profile.points += prize
                inviter.profile.save()
                break
