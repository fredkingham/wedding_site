import json
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from register import serializers


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["user"] = User.objects.first()
        ctx["details"] = JSONRenderer().render(
            serializers.InvitationDetailsSerializer(
                ctx["user"].invitation_details,
                context={'request': self.request}
            ).data,
        )
        ctx["details"] = json.dumps(json.loads(ctx["details"].decode('utf-8')))
        return ctx
