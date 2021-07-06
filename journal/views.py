import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Entry, Activity, Distortion

def index(request):
    return render(request, "journal/index.html")


def login_user(request):
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


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_user(request):
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


@login_required
def edit_user(request, id):
    if request.method == "PUT":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "journal/edit.html", {
                "user": request.user,
                "message": "Passwords must match."
            })
        
        # Attempt to edit user
        try:
            user = request.user
            user.username = username
            user.email = email
            user.password = password
            user.save()
        except IntegrityError:
            return render(request, "journal/register.html", {
                "message": "Username already taken."
            })            
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "journal/edit.html", {
            "user": request.user
        })


@login_required
def delete_user(request, id):
    if request.method == "DELETE":
        request.user.delete()
        HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))


@login_required
def entries(request):
    return render(request, "journal/entries.html")


@login_required
def new_entry(request):
    if request.method == "POST":
        pass

    else:
        return render(request, "journal/new_entry.html", {
            "activities": request.user.activities.all(),
            "distortions": Distortion.objects.all()
        })


@login_required
def entry(request, id):
    pass


@login_required
def edit_entry(request, id):
    if request.method == "PUT":
        pass

    else:
        pass


@login_required
def delete_entry(request, id):
    if request.method == "DELETE":
        pass

    else:
        pass


def distortions(request):
    return render(request, "journal/distortions.html")


@csrf_exempt
@login_required
def new_activity(request):
    if request.method == "POST":
        
        # Load data from request
        data = json.loads(request.body)
        if data.get("name") is not None:
            name = data["name"]
        
        # Check if activity name already exists
        activity = request.user.activities.all().filter(name=name.lower())
        if activity.exists():
            return JsonResponse({
                "error": "Activity already exists."
            }, status=400)
        
        activity = Activity(user=request.user,name=name.lower())
        activity.save()

        return JsonResponse({
            "id": activity.id,
            "name": activity.name
        })

    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


@login_required
def edit_activity(request, id):
    if request.method == "PUT":
        pass
    
    else:
        pass


@login_required
def delete_activity(request, id):
    if request.method == "DELETE":
        pass

    else:
        pass


@login_required
def user_profile(request, id):
    return render(request, "journal/user_profile.html")