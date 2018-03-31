from django.urls import path, include
from django.contrib.auth import views as auth_views
from register import views
from register import api

urlpatterns = [
    path('logout/', auth_views.logout, name='logout'),
    path('', views.HomeView.as_view(), name="home"),
    path('login/', views.Login.as_view(), name="login"),
    path('api/', include(api.router.urls)),
]
