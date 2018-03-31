from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.template.loader import get_template


class Command(BaseCommand):

    def send_mail(self, user, body):
        send_mail(
            "Christina & Fred's wedding - 1 September",
            body,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

    def handle(self, *args, **options):
        tmp = get_template("email_template")



        for user in User.objects.all():
