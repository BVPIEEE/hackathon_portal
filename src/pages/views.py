import os

from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from accounts.models import team, phaseSelectionModel, manageTeam

# Create your views here.
from hackSettings.settings import BASE_DIR


def index(request):
    return render(request, 'pages/index.html')


def scoring_dashboard(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login first for Guest/Mentor")
        return redirect("home")

    try:
        authority = manageTeam.objects.get(user=request.user)
    except ObjectDoesNotExist:
        messages.warning(request, "you are not authorised to access this")
        return redirect("home")
    return render(request, 'pages/scoring.html')


def participant_dashboard(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login using Github first")
        return redirect("home")

    with open("participants.csv", 'r') as file:
        reader = file.read()
        if request.user.username in reader:
            return render(request, 'pages/dashboard.html')
        messages.warning(request, "You are not a participant")
        return redirect("home")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Log out successfully")
    return redirect('home')


def submission1(request):
    try:
        team.objects.get(team_leader_github=request.user.username)
    except ObjectDoesNotExist:
        messages.warning(request, "Only Leader can submit the task")
        return redirect("dashboard")
    return render(request, "pages/submission1.html")


def submission2(request):
    try:
        teamObj = team.objects.get(team_leader_github=request.user.username)
    except ObjectDoesNotExist:
        messages.warning(request, "Only Leader can submit the task")
        return redirect("dashboard")

    try:
        phase = phaseSelectionModel.objects.get(team=teamObj)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.section2:
        return render(request, "pages/submission2.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")


def submission3(request):
    try:
        teamObj = team.objects.get(team_leader_github=request.user.username)
    except ObjectDoesNotExist:
        messages.warning(request, "Only Leader can submit the task")
        return redirect("dashboard")

    try:
        phase = phaseSelectionModel.objects.get(team=teamObj)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.section3:
        return render(request, "pages/submission3.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")


def submission4(request):
    try:
        teamObj = team.objects.get(team_leader_github=request.user.username)
    except ObjectDoesNotExist:
        messages.warning(request, "Only Leader can submit the task")
        return redirect("dashboard")

    try:
        phase = phaseSelectionModel.objects.get(team=teamObj)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.section4:
        return render(request, "pages/submission4.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")


def final(request):
    try:
        teamObj = team.objects.get(team_leader_github=request.user.username)
    except ObjectDoesNotExist:
        messages.warning(request, "Only Leader can submit the task")
        return redirect("dashboard")

    try:
        phase = phaseSelectionModel.objects.get(team=teamObj)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.final:
        return render(request, "pages/final.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")
