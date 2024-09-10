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


@api_view(["PUT"])
def update(request):
    if request.method == "PUT":

        try:
            key = request.data["title"]

            book = Books.objects.filter(title=key)

            # if book.count() != 0:

            #     print(book)

            book.author = request.data["author"]
            book.pub_date = request.data["pub_date"]
            book.save()
            # else:
            #     return Response("Book not found", status=status.HTTP_404_NOT_FOUND)

            return Response("Book updated successfully", status=status.HTTP_200_OK)

        except Books.DoesNotExist:
            return Response("Book not found", status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(type(e))
            return Response(
                "There was an error while updating the Book",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@api_view(["DELETE"])
def delete(request):

    if request.method == "DELETE":
        key = request.data["title"]

        Books.objects.filter(title=key).delete()
