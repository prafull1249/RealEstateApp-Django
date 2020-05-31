from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def register(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "username is already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email is already taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, "User is successfully registered and you can log in now!")
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in now')
            return redirect('dashboard')
    else:
        return render(request, 'accounts/login.html')
    
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are not logged out")
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
