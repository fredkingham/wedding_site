# Generated by Django 2.0 on 2018-04-01 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20180331_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationdetails',
            name='plus_one',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plus_one_invitation_details', to=settings.AUTH_USER_MODEL),
        ),
    ]
