from django.contrib.auth import authenticate
from django.forms.widgets import DateTimeBaseInput
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import CreateStudent, CreateTeacher, NoticeGenerate
from .models import StudentInfo, Staffs, Feedback, TeacherLeave


def home_view(request):
    return render(request, 'principal/home.html')

def admin_sign_up(request):
    if request.method == "POST":
        sp = SignUpForm(request.POST)
        if sp.is_valid():
            user = sp.save()
            user_id = user.pk
            #login(request,sp)
            return HttpResponseRedirect('/admin_login/adminlogin/')
    else:
        sp = SignUpForm()
    return render(request, 'signup.html', {'form':sp})

def admin_user_login(request):
        if request.method == "POST":
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('head')
        else:
            fm = AuthenticationForm()
        return render(request, 'principal/adminlogin.html', {'form':fm})

def head(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        return render(request, 'principal/head.html', {'name':request.user, 'user_name':user_name})
    else:
        return HttpResponseRedirect('/login/admin/')

def admin_logout(request):
    django_logout(request)
    return HttpResponseRedirect('/admin_login/adminlogin/') 

def showformdata(request):
    if request.method == 'POST':
        fm = CreateStudent(request.POST)
        if fm.is_valid():
            fm.save()
            fm = CreateStudent()
    else:
        fm = CreateStudent()
    return render(request, 'studentregistration.html', {'form':fm})


def showdata(request):
    stud = StudentInfo.objects.all()
    return render(request, 'principal/studentsdata.html', {'stu':stud})

def staff_showformdata(request):
    if request.method == 'POST':
        fm = CreateTeacher(request.POST)
        if fm.is_valid():
            fm.save()
            fm = CreateTeacher()
    else:
        fm = CreateTeacher()
    return render(request, 'teacherregistration.html', {'form':fm})


def staff_showdata(request):
    tea = Staffs.objects.all()
    return render(request, 'principal/teacherdata.html', {'tea':tea})

def delete_data(request,id):
    if request.method == 'POST':
        pi = StudentInfo.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/admit/admit/")

def update_data(request,id):
    if request.method == 'POST':
        st = StudentInfo.objects.get(pk=id)
        fm = CreateStudent(request.POST, instance=st)
        if fm.is_valid():
            fm.save()
    else:
        st = StudentInfo.objects.get(pk=id)
        fm = CreateStudent(instance=st)
    return render(request, 'studentregistration.html', {'form':fm})

def delete_data_staff(request,id):
    if request.method == 'POST':
        staff = Staffs.objects.get(pk=id)
        staff.delete()
        return HttpResponseRedirect("/staffdata/staffdata/")

def update_data_staff(request,id):
    if request.method == 'POST':
        st = Staffs.objects.get(pk=id)
        fm = CreateTeacher(request.POST, instance=st)
        if fm.is_valid():
            fm.save()
    else:
        st = Staffs.objects.get(pk=id)
        fm = CreateTeacher(instance=st)
    return render(request, 'teacherregistration.html', {'form':fm})

def create_notice(request):
    if request.method == 'POST':
        fm = NoticeGenerate(request.POST)
        if fm.is_valid():
            fm.save()
            fm = NoticeGenerate()
    else:
        fm = NoticeGenerate()
    return render(request, 'notice.html', {'form':fm})

def show_feed(request):
    tf = Feedback.objects.all()
    return render(request, 'showfeed.html', {'tf':tf})

def show_teaLeave(request):
    tf = TeacherLeave.objects.all()
    return render(request, 'showstaffleave.html', {'tf':tf})

def admin_change_pass(request):
        if request.method == "POST":
            fm = SetPasswordForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/head/head/')
        else:
            fm = SetPasswordForm(user = request.user)
        return render(request, 'changepassadmin.html', {'form':fm})


