from django.urls import path, include


from .views import home

urlpatterns = [
    path("index", view=home, name="home"),
]
