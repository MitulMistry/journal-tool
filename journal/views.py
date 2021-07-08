import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator

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
    entries = request.user.entries.all().order_by("-timestamp")
    p = Paginator(entries, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    
    return render(request, "journal/entries.html", {
        "page_obj": page_obj
    })


@login_required
def new_entry(request):
    if request.method == "POST":

        date = request.POST["date"]
        time = request.POST["time"]
        mood = request.POST["mood"]
        events = request.POST["events"]
        negative_thoughts = request.POST["negative_thoughts"]
        positive_thoughts = request.POST["positive_thoughts"]

        try:
            activities = request.POST.getlist("activities")
        except:
            activities = []

        try:
            distortions = request.POST.getlist("distortions")
        except:
            distortions = []

        # "date": "2021-07-07"
        # "time": "23:24"
        datetime_string = f"{date} {time}"
        timestamp = datetime.strptime(datetime_string, "%Y-%d-%m %H:%M")

        # Attempt to create new Entry
        try:
            entry = Entry(
                user=request.user,
                timestamp=timestamp,
                mood=mood,
                events=events,
                negative_thoughts=negative_thoughts,
                positive_thoughts=positive_thoughts
            )
            entry.save()

            # Associations need to be established after entry is saved
            for activity_id in activities:
                activity = Activity.objects.get(pk=int(activity_id), user=request.user)
                entry.activity_set.add(activity)

            for distortion_id in distortions:
                distortion = Distortion.objects.get(pk=int(distortion_id))
                entry.distortion_set.add(distortion)

        except:
            return render(request, "journal/new_entry.html", {
                "activities": request.user.activities.all(),
                "distortions": Distortion.objects.all(),
                "message": "Entry creation failed."
            })

        return HttpResponseRedirect(reverse("entries"))

    else:
        return render(request, "journal/new_entry.html", {
            "activities": request.user.activities.all(),
            "distortions": Distortion.objects.all()
        })


@login_required
def entry(request, id):

    # Query for requested Entry
    try:
        entry = Entry.objects.get(pk=id)
    except:
        return render(request, "journal/index.html", {
            "message": "Entry not found."
        })

    return render(request, "journal/entry.html", {
        "entry": entry
    })


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
    return render(request, "journal/distortions.html", {
        "distortions": Distortion.objects.all()
    })


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
def user_profile(request):
    user = request.user
    return render(request, "journal/user_profile.html", {
        "user": user,
        "top_distortions": user.top_distortions(),
        "top_activities": user.top_activities(),
        "recent_entries": user.recent_entries()
    })