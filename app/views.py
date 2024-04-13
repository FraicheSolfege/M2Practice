from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from .team_info import TEAMS

# Create your views here.


def home_page(request):
    return render(request, "home.html", {"teams": TEAMS})


def team_page(request, teamName):
    return render(request, "teamdetails.html", {"team": TEAMS[teamName]})