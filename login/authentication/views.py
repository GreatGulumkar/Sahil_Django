from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from django.contrib.auth import login, logout


@api_view(["POST"])
def user_register(request):
    if request.method == "POST":
        try:
            User.objects.create(
                first_name=request.data["first_name"],
                username=request.data["username"],
                password=request.data["password"],
            )

            return Response("User created successfully", status=status.HTTP_200_OK)
        except:
            return Response(
                "Oops! Something went worng", status=status.HTTP_400_BAD_REQUEST
            )


@api_view(["POST"])
def user_login(request):
    if request.method == "POST":
        try:
            valid_user = User.objects.get(
                username=request.data["username"],
                password=request.data["password"],
            )

            login(request, valid_user)

            return Response(f"{request.data["username"]} created logged in", status=status.HTTP_200_OK)
        except:
            return Response(
                "Oops! Something went worng", status=status.HTTP_400_BAD_REQUEST
            )


@api_view(["GET"])
def user_logout(request):
    if request.method == "GET":
        logout(request)

        return Response("User logged out", status=status.HTTP_200_OK)


@api_view(["GET"])
def user_check(request):
    if request.method == "GET":
        cur_user = request.user 
        return Response(f"{cur_user.username}")
