from django.shortcuts import render, redirect

from django.shortcuts import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from .models import Userdata

# Create your views here.


@csrf_exempt
def register_user(request):

    if request.method == "POST":

        try:
            firstname = request.POST["Firstname"]
            lastname = request.POST["Lastname"]
            password = request.POST["confirm-password"]

            Userdata.objects.create(
                firstname=firstname,
                lastname=lastname,
                password=password,
            )

            return redirect("login")
        except Exception as e:
            print(e)
            return HttpResponse("Something went wrong")


@csrf_exempt
def signup(request):

    return render(request, "signup.html")
