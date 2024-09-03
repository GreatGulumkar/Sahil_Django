from django.shortcuts import render
from django.shortcuts import HttpResponse

from register.models import Userdata
from django.views.decorators.csrf import csrf_exempt


def login(request):
    return render(request, "login.html")


@csrf_exempt
def check_login(request):

    try:
        data = Userdata.objects.filter(
            firstname=request.POST["firstname"], password=request.POST["password"]
        )

        if data:
            return HttpResponse("User Authenticated")
        else:
            HttpResponse("Invalid cridentials")
    except:
        return HttpResponse("Something went wrong")
