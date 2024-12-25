from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        

        if user is not None:
            login(request,user)
            messages.success(request, f"Welcome, {username}!")
            return render(request, 'home.html')
        else:
            messages.warning(request, f"login failed, {username}!")
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if password != confirm_password:
            messages.error(request, "password doesn't match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "this username already exists")
        if password == confirm_password:
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password
            )
            print("registration successfull")
        else:
            print("registration failed")    

    return render(request, 'signup.html')