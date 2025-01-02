from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def goodbye(request):
    return render(request, "hello/goodbye.html")

def numero(request, num):
    return HttpResponse(f"The number is: {num}.")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })