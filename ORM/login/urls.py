from django.urls import path

from .views import *

urlpatterns = [
    path("", view=login, name="login"),
    path("check/", view=check_login, name="check_login"),
]
