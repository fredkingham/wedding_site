from django.core.mail import send_mail
from django.template.loader import get_template
from sesame import utils

SUBJECT = "Christina & Fred's wedding - 1 September"
FROM_EMAIL = "christinaandfredding@gmail.com"


def send_invite(user):
    tmp = get_template("email_template")
    params = utils.get_query_string(user)
    content = tmp.render(dict(user=user, params=params))
    send_mail(
        SUBJECT,
        content,
        [user.email],
        fail_silently=False
    )
