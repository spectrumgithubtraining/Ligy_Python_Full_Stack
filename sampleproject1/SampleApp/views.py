from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"login.html")


def reg(request):
    return render(request,"registration.html")

def forgot(request):
    return render(request,"forgotpassword.html")

# Create your views here.
