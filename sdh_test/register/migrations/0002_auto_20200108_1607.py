# Generated by Django 2.2 on 2020-01-08 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='inviter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='invitation_code',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
