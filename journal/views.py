from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Entry, Activity, Distortion

def index(request):
    return render(request, "journal/index.html")


def login(request):
    if request.method == "POST":
        
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "journal/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "journal/login.html")


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "journal/register.html", {
                "message": "Passwords must match."
            })
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "journal/register.html", {
                "message": "Username already taken."
            })            
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "journal/register.html")


def edit(request):
    if request.method == "PUT":
        pass

    else:
        return render(request, "journal/register.html")


def delete(request):
    if request.method == "DELETE":
        pass
    
    else:
        return HttpResponseRedirect(reverse("index"))


def new_entry(request):
    if request.method == "POST":
        pass

    else:
        return render(request, "journal/new_entry.html")


def entry(request, id):
    pass


def edit_entry(request, id):
    if request.method == "PUT":
        pass

    else:
        pass


def delete_entry(request, id):
    if request.method == "DELETE":
        pass

    else:
        pass


def distortions(request):
    return render(request, "journal/distortions.html")


def new_activity(request):
    if request.method == "POST":
        pass

    else:
        pass


def edit_activity(request, id):
    if request.method == "PUT":
        pass
    
    else:
        pass


def delete_activity(request, id):
    if request.method == "DELETE":
        pass

    else:
        pass


def user_profile(request, id):
    return render(request, "journal/user_profile.html")