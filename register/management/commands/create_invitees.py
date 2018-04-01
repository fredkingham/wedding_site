import os
import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

INVIATION_FILE_DIR = os.path.join(settings.BASE_DIR, "data")

FIRST_NAME = "First name"
SECOND_NAME = "Second name"
EMAIL_ADDRESS = "Email address"
PLUS_ONE = "Partner's email address"


def process_row(csv_row):
    print("=" * 20)
    print(csv_row)
    print("=" * 20)
    email = csv_row[EMAIL_ADDRESS].strip()

    if email == "???" or email == "????":
        return

    user, _ = User.objects.get_or_create(
        email=email,
        username=email
    )
    user.first_name = csv_row[FIRST_NAME].strip()
    user.last_name = csv_row[SECOND_NAME].strip()
    user.save()

    plus_one = csv_row.get(PLUS_ONE, "").strip()
    if plus_one and not plus_one == "???" and not plus_one == "????":
        plus_one_user, _ = User.objects.get_or_create(
            email=plus_one,
            username=plus_one
        )

        invitationdetails = user.invitation_details
        invitationdetails.plus_one = plus_one_user
        invitationdetails.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.filter(is_superuser=False).delete()
        all_invitation_files = [
            i for i in os.listdir(INVIATION_FILE_DIR) if i.endswith(".csv")
        ]
        for all_invitation_file in all_invitation_files:
            full_path = os.path.join(INVIATION_FILE_DIR, all_invitation_file)
            with open(full_path) as csv_file:
                reader = csv.DictReader(csv_file)
                for csv_row in reader:
                    process_row(csv_row)
