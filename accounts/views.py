from django.contrib import auth, messages
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        id = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(username=id, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('scoring')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'pages/login.html')
