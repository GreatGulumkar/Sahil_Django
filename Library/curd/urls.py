from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("book/create/", views.book_create, name="book_create"),
    path(
        "book/update/<int:book_id>/<str:title>", views.book_update, name="book_update"
    ),
    path("book/delete/<int:book_id>/", views.book_delete, name="book_delete"),
]
