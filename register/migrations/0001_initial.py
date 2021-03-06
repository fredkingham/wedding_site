# Generated by Django 2.0 on 2018-03-29 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_choice', models.CharField(blank=True, choices=[('pig', 'pig'), ('veggie', 'veggie'), ('other', 'other')], default='', max_length=256)),
                ('rsvp_choice', models.NullBooleanField()),
                ('visited', models.BooleanField(default=False)),
                ('food_preference_other', models.TextField()),
                ('song_choice', models.TextField()),
                ('plus_one', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, parent_link=True, related_name='plus_one_invitation_details', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invitation_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
