from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import IceCream

def home(request):
    ice_creams = IceCream.objects.all()
    for ice_cream in ice_creams:
        print(f"ID: {ice_cream.id}, Name: {ice_cream.name}, Flavor: {ice_cream.flavor}, Price: {ice_cream.price}")
    return render(request, "L7App/home.html", {'ice_creams': ice_creams})


def cart(request):
    context={}
    return render (request,"L7App/cart.html",context)


# Registration view
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'L7App/register.html')

# Login view
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'L7App/login.html')

# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
def suggestions(request):
    return render(request, "L7App/suggestions.html")

def submit_suggestion(request):
    if request.method == 'POST':
        flavor = request.POST.get('flavor')
        allergy = request.POST.get('allergy')
        # Save the data or process as needed
        print(f"Flavor: {flavor}, Allergy: {allergy}")
        return HttpResponse("Thank you for your submission!")
    return HttpResponse("Invalid request")
