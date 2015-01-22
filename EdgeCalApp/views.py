from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the EdgeCal index.")

def detail(request, user_id):
    response = "You're looking at user %s."
    return HttpResponse(response % user_id)

def results(request, user_id):
    response = "You're looking at results of user %s."
    return HttpResponse(response % user_id)

def vote(request, user_id):
    return HttpResponse("You're looking at user vote %s." % user_id)