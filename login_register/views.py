from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def view_base(request):
    resp=render(request, 'login_register/base.html')
    return resp



def view_register(request):
    
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username is already taken")
            return redirect('/login_register/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
            )
        
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully")

        return redirect('/login_register/')
    return render(request , 'login_register/register.html')



def view_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login_register/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login_register/login/')
        
        else:
            login(request, user)
            return redirect('/login_register/')
        

    return render(request , 'login_register/login.html')


def view_logout(request):
    logout(request)
    return redirect('/login_register/')