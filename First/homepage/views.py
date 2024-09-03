from django.shortcuts import render

from django.shortcuts import HttpResponse

from django.http import JsonResponse


# Create your views here.


def home(request):
    return render(request, "home.html")


def displayname(request):
    name = request.GET["username"]
    print(name)
    # return render(request, "name.html", {"username": name})
    return HttpResponse(name)
    # return JsonResponse({"username": name})
