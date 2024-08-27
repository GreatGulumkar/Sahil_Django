from django.urls import path, include


from .views import sign_up, log_in

urlpatterns = [
    path("signup", view=sign_up, name="sign_up"),
    path("login", view=log_in, name="log_in"),
]
