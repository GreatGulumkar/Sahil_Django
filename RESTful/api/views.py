from django.shortcuts import render
from django.core.serializers import serialize
from database.models import Books

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST", "GET"])
def create_api(request):
    if request.method == "POST":
        try:
            title = request.data["title"]
            author = request.data["author"]
            pub_date = request.data["pub_date"]

            Books.objects.create(
                title=title,
                author=author,
                pub_date=pub_date,
            )

            return Response("Book added successfully", status=status.HTTP_200_OK)
        except:
            return Response(
                "There was an error while creating the Book",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    if request.method == "GET":
        return Response("Please use POST method")


@api_view(["GET"])
def read(request):
    if request.method == "GET":
        data = Books.objects.all()

        serial = serialize("json", data)

        return Response(serial, status=status.HTTP_200_OK)


def update(request):
    pass


def delete(request):
    pass
