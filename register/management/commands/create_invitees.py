from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        cara = User.objects.create(
            username="Cara",
            first_name="Cara",
            last_name="Curren"
        )
        cathy = User.objects.create(
            username="Cathy",
            first_name="Cathy",
            last_name="Rushworth"
        )
        invitation_details = cara.invitation_details
        invitation_details.plus_one = cathy
        invitation_details.save()
