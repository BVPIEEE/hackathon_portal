import os
from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from accounts.models import team, phaseSelectionModel, manageTeam
from complexModules.models import scoringModel, gradeModel, currentRound, submissionModel, roundDetails
from .forms import scoringForm, gradeForm, submissionForms, youtubeForms, roundDetailsForm
from .models import youtubeModel
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

    obj = scoringModel.objects.all()
    form = scoringForm(obj[0])
    round = currentRound.objects.all()
    
    try:
        obj = gradeModel.objects.get(round=round[0].round)
    except ObjectDoesNotExist:
        messages.warning(request,"This is server side problem, Kindly contact to the WIEHACK 2.0 Team")
        return redirect('dashboard')

    form2 = gradeForm(obj)

    if round[0].round > 4:
            return render(request, 'pages/judge_scoring.html', {'form':form.data,'form2':form2.data})
    return render(request, 'pages/scoring1.html', {'form': form.data, 'form2':form2.data})

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
    model = youtubeModel.objects.all()
    form = youtubeForms(model[0])
    round = currentRound.objects.all()
    
    # round details
    try:
        obj = roundDetails.objects.get(round = round[0].round)
    except ObjectDoesNotExist:
        messages.warning(request,"This is server side problem, Kindly contact to the WIEHACK 2.0 Team")
        return redirect('about')
        
    form2 = roundDetailsForm(obj)
    return render(request, 'pages/dashboard.html', {"form":form.data, "round":round[0].round, "form2":form2.data})


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Log out successfully")
    return redirect('home')


def submission1(request):
    if request.user.is_anonymous:
        messages.warning(request, "Login through Github First")
        return redirect("dashboard")
        
    team = get_team(request)
    if team is False:
        messages.warning(request, "You are not the participant")
        return redirect("dashboard")

    phase = phaseSelectionModel.objects.get(team=team)
    round = currentRound.objects.all()

    if round[0].round == phase.round:
        try:
            obj = submissionModel.objects.get(round=round[0].round)
        except ObjectDoesNotExist:
            messages.warning(request, "Its a server side error, please contact the WIEHACK 2.0 Team")
            return redirect("dashboard")
            
        form2 = submissionForms(obj)
        return redirect(form2.data.form_link)
        # return render(request, "pages/submission1.html", {"form":form2.data}) # because google form not working
    
    messages.warning(request,"You have not yet qualified for this round")
    return redirect("dashboard")


def about(request):
    model = youtubeModel.objects.all()
    form = youtubeForms(model[0])
    return render(request, "pages/about.html", {"form":form.data})

def themes(request):
    return render(request, "pages/themes.html")

def info(request):
    return render(request, "pages/general_ins.html")