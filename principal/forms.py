from django import forms
from django.forms import widgets
from django.forms.widgets import PasswordInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentInfo, Staffs, Assignment, Feedback, Notice, StudentLeave, TeacherLeave

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'


class CreateTeacher(forms.ModelForm):
    class Meta:
        model = Staffs
        fields = '__all__'


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Retype Password', widget= PasswordInput)
    class Meta:
        model = User
        fields = ['username']

class Assignment(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject','homework']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

class NoticeGenerate(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'

class StudentLeave(forms.ModelForm):
    class Meta:
        model = StudentLeave
        fields = '__all__'

class TeacherLeave(forms.ModelForm):
    class Meta:
        model = TeacherLeave
        fields = '__all__'