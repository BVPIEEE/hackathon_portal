from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def update(request):
    return HttpResponse("hello", status=200)
