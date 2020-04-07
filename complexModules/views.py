from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from threading import Thread
from django.template.loader import render_to_string
from accounts.models import manageTeam, team
from django.contrib.auth import get_user_model

# Create your views here.
def update(request):
    return HttpResponse("hello", status=200)

def email(request):
    if request.user.is_anonymous:
        messages.warning(request,"Login first")
        return redirect("dashboard")
    
    if request.method == "POST":
        teamname = request.POST['teamname']
        email = request.POST['email']
        msg = request.POST['msg']

        try:
            manageTeam.objects.get(user = request.user)
        except:
            message = render_to_string('../template/email/support.html', {
                'teamname': teamname,
                'email': email,
                'msg': msg
            })

            mail_subject = 'Participant requested support' + ' Team: '+ teamname
            email = EmailMessage(mail_subject, message, to=['bvpieee.info@gmail.com'])

            Thread(target=email.send, args=()).start()
            messages.success(request, "your msg sent to the team")
            return redirect('dashboard')
        
        # for guests and judges
        try:
            obj=team.objects.get(team_name = teamname)
        except:
            messages.warning(request, 'Team does not exist, please write correct teamname(Case sensitive)')
            return redirect('scoring')
        
        try:
            user1 = get_user_model().objects.get(username = obj.team_leader_github)
        except:
            message.warning(request,"user does not exist please contact BVPIEEE Support")
            return redirect('scoring')
        
        message = render_to_string('../template/email/guest.html', {
            'teamname': teamname,
            'email': email,
            'msg': msg
        })

        mail_subject = 'Suggestion from Guest and Mentor to ' + ' Team: '+ teamname
        email = EmailMessage(mail_subject, message, to=[user1.email])

        Thread(target=email.send, args=()).start()
        messages.success(request, "your msg sent to the team, thanks for the support")
        return redirect('scoring')