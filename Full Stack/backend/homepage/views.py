from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ItinerarySerializer

from homepage.models import Itinerary


@api_view(["GET"])
def ShowItinerary(request):
    if request.method == "GET":
        data = Itinerary.objects.all()
        serializer = ItinerarySerializer(data, many=True)

        return Response(serializer.data)


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(["POST"])
def create_itinerary(request):
    if request.method == "POST":
        try:
            print(request.data["title"])
            print(request.data["description"])

            Itinerary.objects.create(
                title=request.data["title"],
                description=request.data["description"],
            )

            return Response(
                {"message": "Itinerary created successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {"message": "Itinerary not created successfully"},
                status=status.HTTP_400_BAD_REQUEST,
            )
