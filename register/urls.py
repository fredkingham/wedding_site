from django.urls import path, include
from register import views
from register import api

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path(r'api/', include(api.router.urls)),
]
