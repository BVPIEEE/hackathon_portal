import os

from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from accounts.models import team, phaseSelectionModel, manageTeam
from complexModules.models import scoringModel
from .forms import scoringForm
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

    obj = scoringModel.objects.get(scoringNumber=1)
    form = scoringForm(obj)
    return render(request, 'pages/scoring1.html', {'form': form.data})


def scoring_dashboard2(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login first for Guest/Mentor")
        return redirect("home")

    try:
        authority = manageTeam.objects.get(user=request.user)
    except ObjectDoesNotExist:
        messages.warning(request, "you are not authorised to access this")
        return redirect("home")

    obj = scoringModel.objects.get(scoringNumber=2)
    form = scoringForm(obj)
    return render(request, 'pages/scoring2.html', {'form': form.data})


def scoring_dashboard3(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login first for Guest/Mentor")
        return redirect("home")

    try:
        authority = manageTeam.objects.get(user=request.user)
    except ObjectDoesNotExist:
        messages.warning(request, "you are not authorised to access this")
        return redirect("home")

    obj = scoringModel.objects.get(scoringNumber=3)
    form = scoringForm(obj)
    return render(request, 'pages/scoring3.html', {'form': form.data})


def scoring_dashboard4(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login first for Guest/Mentor")
        return redirect("home")

    try:
        authority = manageTeam.objects.get(user=request.user)
    except ObjectDoesNotExist:
        messages.warning(request, "you are not authorised to access this")
        return redirect("home")

    obj = scoringModel.objects.get(scoringNumber=4)
    form = scoringForm(obj)
    return render(request, 'pages/scoring4.html', {'form': form.data})


def scoring_dashboardFinal(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login first for Guest/Mentor")
        return redirect("home")

    try:
        authority = manageTeam.objects.get(user=request.user)
    except ObjectDoesNotExist:
        messages.warning(request, "you are not authorised to access this")
        return redirect("home")

    obj = scoringModel.objects.get(scoringNumber=5)
    form = scoringForm(obj)
    return render(request, 'pages/scoringFinal.html', {'form': form.data})

def get_team(request):
    try:
        return team.objects.get(team_leader_github=request.user.username)
    except ObjectDoesNotExist:
        try:
            return team.objects.get(member1_github=request.user.username)
        except ObjectDoesNotExist:
            try:
                return team.objects.get(member2_github=request.user.username)
            except ObjectDoesNotExist:
                try:
                    return team.objects.get(member3_github=request.user.username)
                except ObjectDoesNotExist:
                    return False

def participant_dashboard(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login using Github first")
        return redirect("home")
    
    if get_team(request) is False:
        messages.warning(request, "You are not a participant")
        return redirect("home")
    
    return render(request, 'pages/dashboard.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Log out successfully")
    return redirect('home')


def submission1(request):
    # try:
    #     team.objects.get(team_leader_github=request.user.username)
    # except ObjectDoesNotExist:
    #     messages.warning(request, "Only Leader can submit the task")
    #     return redirect("dashboard")

    if get_team(request) is False:
        messages.warning(request, "You are not the participant")
        return redirect("home")

    return render(request, "pages/submission1.html")


def submission2(request):
    # try:
    #     team = team.objects.get(team_leader_github=request.user.username)
    # except ObjectDoesNotExist:
    #     messages.warning(request, "Only Leader can submit the task")
    #     return redirect("dashboard")

    # 2nd method
    team = get_team(request)

    if team is False:
        messages.warning(request, "You are not the participant")
        return redirect("home")

    try:
        phase = phaseSelectionModel.objects.get(team=team)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.section2:
        return render(request, "pages/submission2.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")


def submission3(request):
    # try:
    #     team = team.objects.get(team_leader_github=request.user.username)
    # except ObjectDoesNotExist:
    #     messages.warning(request, "Only Leader can submit the task")
    #     return redirect("dashboard")

    # 2nd method
    team = get_team(request)

    if team is False:
        messages.warning(request, "You are not the participant")
        return redirect("home")

    try:
        phase = phaseSelectionModel.objects.get(team=team)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.section3:
        return render(request, "pages/submission3.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")


def submission4(request):
    # try:
    #     team = team.objects.get(team_leader_github=request.user.username)
    # except ObjectDoesNotExist:
    #     messages.warning(request, "Only Leader can submit the task")
    #     return redirect("dashboard")

    # 2nd method
    team = get_team(request)

    if team is False:
        messages.warning(request, "You are not the participant")
        return redirect("home")

    try:
        phase = phaseSelectionModel.objects.get(team=team)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.section4:
        return render(request, "pages/submission4.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")


def final(request):
    # try:
    #     team = team.objects.get(team_leader_github=request.user.username)
    # except ObjectDoesNotExist:
    #     messages.warning(request, "Only Leader can submit the task")
    #     return redirect("dashboard")

    # 2nd method
    team = get_team(request)

    if team is False:
        messages.warning(request, "You are not the participant")
        return redirect("home")

    try:
        phase = phaseSelectionModel.objects.get(team=team)
    except ObjectDoesNotExist:
        messages.warning(request, "You cannot access this section")
        return redirect("dashboard")

    if phase.final:
        return render(request, "pages/final.html")
    else:
        messages.warning(request, "You have not yet qualified in this round")
        return redirect("dashboard")
