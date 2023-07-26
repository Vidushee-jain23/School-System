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
from .forms import Assignment,TeacherLeave,CreateTeacher
from .models import StudentLeave,Staffs

def teacher_sign_up(request):
    if request.method == "POST":
        sp = SignUpForm(request.POST)
        if sp.is_valid():
            sp.save()
            return HttpResponseRedirect('/teacher_login/teacherlogin/')
    else:
        sp = SignUpForm()
    return render(request, 'teacher_sign.html', {'form':sp})

def teacher_user_login(request):
        if request.method == "POST":
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('teacherhome')
        else:
            fm = AuthenticationForm()
        return render(request, 'principal/teacherlogin.html', {'form':fm})


def teacher_home(request):
    if request.user.is_authenticated:
       user_name = request.user.username
       return render(request, 'principal/teacherhome.html', {'name':request.user,'user_name':user_name})
    else:
        return HttpResponseRedirect('/teacher_login/teacherlogin') 
    
def teacher_logout(request):
    django_logout(request)
    return HttpResponseRedirect('/teacher_login/teacherlogin/')

def assign_student(request):
    if request.method == 'POST':
        hw = Assignment(request.POST)
        if hw.is_valid():
            hw.save()
            hw = Assignment()
    else:
        hw = Assignment()
    return render(request, 'teacherAssign.html', {'form':hw})

def leave_request(request):
    if request.method == 'POST':
        hw = TeacherLeave(request.POST)
        if hw.is_valid():
            hw.save()
            hw = TeacherLeave()
    else:
        hw = TeacherLeave()
    return render(request, 'teacherLeave.html', {'form':hw})

def show_studLeave(request):
    tf = StudentLeave.objects.all()
    return render(request, 'showstudleave.html', {'tf':tf})

def staff_change_pass(request):
        if request.method == "POST":
            fm = SetPasswordForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/teacher/teacherhome/')
        else:
            fm = SetPasswordForm(user = request.user)
        return render(request, 'changepassstaff.html', {'form':fm})