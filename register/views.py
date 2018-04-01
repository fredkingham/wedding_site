import json
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.mixins import LoginRequiredMixin
from register import serializers


class Login(RedirectView):
    url = reverse_lazy("home")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["user"] = self.request.user
        from django.contrib.auth.models import User
        ctx["user"] = User.objects.filter(first_name='Charles').last()
        ctx["details"] = JSONRenderer().render(
            serializers.InvitationDetailsSerializer(
                ctx["user"].invitation_details,
                context={'request': self.request}
            ).data,
        )
        ctx["details"] = json.dumps(json.loads(ctx["details"].decode('utf-8')))
        return ctx
