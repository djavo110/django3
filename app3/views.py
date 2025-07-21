from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    coun = Country.objects.all()
    city = City.objects.all()

    context = {
        "title": "NEW TITLE",
        "coun": coun,
        "city": city

    }
    return render(request, "index.html", context=context)

