from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ItinerarySerializer

from homepage.models import Itinerary


@api_view(["GET"])
def ShowItinerary(request):
    if request.method == "GET":
        data = Itinerary.objects.all()
        serializer = ItinerarySerializer(data, many=True)

        # print(serializer.data)

        json = {
            "Home": "page",
            "name": "Sahil",
            "Course": "Django",
        }
        return Response(serializer.data)
