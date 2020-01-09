from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,
                                primary_key=True,
                                on_delete=models.CASCADE)
    inviter = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="referals")
    invitation_code = models.CharField(
                                max_length=128,
                                default='')
    points = models.IntegerField(default=0)

    def __str__(self):
        return '{} profile'.format(self.user.username)
