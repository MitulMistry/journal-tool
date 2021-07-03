from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, "journal/index.html")


def login(request):
    if request.method == "POST":
        pass

    else:
        return render(request, "journal/login.html")


def logout(request):    
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        pass

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