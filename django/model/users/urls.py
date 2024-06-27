from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.common_login, name="login"),
    path("", views.index, name="index"),
    path("logout/", views.common_logout, name="logout"),
]
