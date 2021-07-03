from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Journal Tool index page.")


def login(request):
    pass


def logout(request):
    pass


def register(request):
    pass


def delete(request):
    pass


def new_entry(request):
    pass


def entry(request, id):
    pass


def edit_entry(request, id):
    pass


def delete_entry(request, id):
    pass


def distortions(request):
    pass


def new_activity(request):
    pass


def edit_activity(request, id):
    pass


def delete_activity(request, id):
    pass


def user_profile(request, id):
    pass