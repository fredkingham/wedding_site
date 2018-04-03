from django.contrib import admin
from register.models import InvitationDetails
from register.send_email import send_invite


class InvitationDetailsAdmin(admin.ModelAdmin):
    actions = ["send_invite", "reset_user"]

    list_display = [
        'username',
        'plus_one',
        'rsvp_choice',
        'invite_sent',
        'visited',
        'food_choice',
        'food_preference_other',
        'song_choice'
    ]
    list_filter = ['invite_sent', 'rsvp_choice']

    def username(self, obj):
        return obj.user.username

    def plus_one(self, obj):
        return obj.plus_one.username

    def send_invite(self, request, queryset):
        for invitation_details in queryset:
            send_invite(invitation_details.user)

    def reset_user(self, request, queryset):
        queryset.update(
            food_choice="",
            invite_sent=None,
            rsvp_choice=None,
            visited=False,
            food_preference_other="",
            song_choice=""
        )


admin.site.register(InvitationDetails, InvitationDetailsAdmin)
