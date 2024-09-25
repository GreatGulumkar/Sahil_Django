from django.urls import path

from .views import *

urlpatterns = [
    path("", view=ShowItinerary, name="ShowItinerary"),
    path("hello-world/", hello_world, name="hello_world"),
    path("create/", create_itinerary, name="create_itinerary"),
]
