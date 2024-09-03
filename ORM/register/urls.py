from django.urls import path

from .views import *

urlpatterns = [
    path("signup", view=signup, name="signup"),
    path("register_user", view=register_user, name="register_user"),
]
