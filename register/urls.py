from django.urls import path, include
from register import views
from register import api

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.HomeView.as_view(), name="home"),
    path('rsvp/', views.Login.as_view(), name="rsvp"),
    path('not_me/', views.Logout.as_view(), name="not_me"),
    path('api/', include(api.router.urls)),
]
