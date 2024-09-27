from django.urls import path

from .views import *

urlpatterns = [
    path("user_register", view=user_register, name="user_register"),
    path("user_login", view=user_login, name="user_login"),
    path("user_logout", view=user_logout, name="user_logout"),
    path("user_logout", view=user_logout, name="user_logout"),
    path("user_check", view=user_check, name="user_check"),
]
