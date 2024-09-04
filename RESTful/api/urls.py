from django.urls import path

from .views import *

urlpatterns = [
    path("create", view=create_api, name="create"),
    path("update", view=update, name="update"),
    path("delete", view=delete, name="delete"),
    path("read", view=read, name="read"),
]
