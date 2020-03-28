from django.contrib import auth
from django.core.checks import messages
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect('home')
