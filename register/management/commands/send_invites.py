from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from register.send_email import send_invite


class Command(BaseCommand):
    def handle(self, *args, **options):
        for user in User.objects.all():
            send_invite(user)
