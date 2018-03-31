from rest_framework import viewsets
from register import models
from register import serializers
from rest_framework.routers import DefaultRouter


class InvitationDetailsViewSet(
    viewsets.ModelViewSet
):
    base_name = "invitationdetails"
    queryset = models.InvitationDetails.objects.all()
    serializer_class = serializers.InvitationDetailsSerializer


router = DefaultRouter()

router.register(
    InvitationDetailsViewSet.base_name,
    InvitationDetailsViewSet,
    InvitationDetailsViewSet.base_name
)
