from django.contrib.auth import authenticate
from django.forms.widgets import DateTimeBaseInput
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import FeedbackForm, StudentLeave
from .models import Notice, Assignment

def student_sign_up(request):
    if request.method == "POST":
        sp = SignUpForm(request.POST)
        if sp.is_valid():
            sp.save()
            #login(request,sp)
            return HttpResponseRedirect('/student_login/studentlogin/')
    else:
        sp = SignUpForm()
    return render(request, 'student_sign.html', {'form':sp})


def student_user_login(request):
        if request.method == "POST":
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('studenthome')
        else:
            fm = AuthenticationForm()
        return render(request, 'principal/studentlogin.html', {'form':fm})


def student_view(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        return render(request, 'principal/studenthome.html', {'name':request.user, 'user_name':user_name})
    else:
        return HttpResponseRedirect('/student_login/studentlogin') 
    

def student_logout(request):
    django_logout(request)
    return HttpResponseRedirect('/student_login/studentlogin/')

def create_feed(request):
    if request.method == 'POST':
        hw = FeedbackForm(request.POST)
        if hw.is_valid():
            hw.save()
            hw = FeedbackForm()
    else:
        hw = FeedbackForm()
    return render(request, 'feed.html', {'form':hw})


def show_notice(request):
    tf = Notice.objects.all()
    return render(request, 'shownotice.html', {'tf':tf})

def show_assignment(request):
    tf = Assignment.objects.all()
    return render(request, 'showassign.html', {'tf':tf})

def leave_requeststu(request):
    if request.method == 'POST':
        hw = StudentLeave(request.POST)
        if hw.is_valid():
            hw.save()
            hw = StudentLeave()
    else:
        hw = StudentLeave()
    return render(request, 'studentLeave.html', {'form':hw})

def stud_change_pass(request):
        if request.method == "POST":
            fm = SetPasswordForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/student/studenthome/')
        else:
            fm = SetPasswordForm(user = request.user)
        return render(request, 'changepassstud.html', {'form':fm})