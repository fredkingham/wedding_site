from django.core.mail import send_mail
from django.utils import timezone
from django.template.loader import get_template
from sesame import utils

SUBJECT = "Christina & Fred's wedding - 1 September"
FROM_EMAIL = "christinaandfredding@gmail.com"


def send_invite(user):
    tmp = get_template("email_template.html")
    params = utils.get_query_string(user)
    content = tmp.render(dict(user=user, params=params))
    id = user.invitation_details
    id.invite_sent = timezone.now()
    user.save()
    send_mail(
        SUBJECT,
        "please come to our wedding",
        'Christina & Fred',
        [user.email],
        fail_silently=False,
        html_message=content
    )
