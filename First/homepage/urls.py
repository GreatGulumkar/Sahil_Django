from django.urls import path, include


from .views import *

urlpatterns = [
    path("", view=home, name="home"),
    path("name", view=displayname, name="displayname"),
]
