from django.contrib.auth.models import User
from rest_framework import serializers
from register import models


class AbstractInvitationDetailsSerializer(object):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_first_name(self, obj):
        return self.obj.user.first_name

    def get_last_name(self, obj):
        return self.obj.user.last_name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class PlusOneSerializer(
    serializers.ModelSerializer,
    AbstractInvitationDetailsSerializer
):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.InvitationDetails
        exclude = ["plus_one"]


class InvitationDetailsSerializer(
    serializers.ModelSerializer
):
    plus_one = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.InvitationDetails
        fields = "__all__"

    def get_plus_one(self, obj):
        invitation_details = models.InvitationDetails.objects.filter(
            plus_one=obj.user
        ).first()
        if invitation_details:
            return PlusOneSerializer(
                invitation_details
            ).data
