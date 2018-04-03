from django.db import models, transaction
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


_FOOD_CHOICES = [
    "pig",
    "veggie",
    "other"
]

FOOD_CHOICES = [(i, i,) for i in _FOOD_CHOICES]


class InvitationDetails(models.Model):
    food_choice = models.CharField(
        max_length=256,
        blank=True,
        default="",
        choices=FOOD_CHOICES
    )
    invite_sent = models.DateTimeField(blank=True, null=True)
    rsvp_choice = models.NullBooleanField()
    visited = models.BooleanField(
        default=False
    )
    food_preference_other = models.TextField(blank=True, default="")
    song_choice = models.TextField(blank=True, default="")
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="invitation_details"
    )
    plus_one = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="plus_one_invitation_details"
    )

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.plus_one:
            po = self.plus_one.invitation_details.plus_one
            if po:
                if not po == self.user:
                    raise ValueError(
                        "a single user can only have one plus one"
                    )
            else:
                invitation_details = self.plus_one.invitation_details
                invitation_details.plus_one = self.user
                invitation_details.save()


@receiver(post_save, sender=User)
def my_callback(sender, instance, *args, **kwargs):
    if not InvitationDetails.objects.filter(user=instance).exists():
        InvitationDetails.objects.create(user=instance)
