# Generated by Django 2.2 on 2020-01-09 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20200109_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='inviter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referal', to=settings.AUTH_USER_MODEL),
        ),
    ]
