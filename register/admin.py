from django.contrib import admin
from register.models import InvitationDetails


class InvitationDetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(InvitationDetails, InvitationDetailsAdmin)
