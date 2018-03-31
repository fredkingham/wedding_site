from django.core.mail import send_mail
from django.template.loader import get_template

SUBJECT = "Christina & Fred's wedding - 1 September"
FROM_EMAIL = "christinaandfredding@gmail.com"


def send_invite(user):
    tmp = get_template("email_template")
    content = tmp.render(user)
    send_mail(
        SUBJECT,
        content,
        [user.email],
        fail_silently=False
    )
