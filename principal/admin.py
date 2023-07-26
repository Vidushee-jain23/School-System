from django.contrib import admin
from .models import StudentInfo,Staffs,Assignment,Feedback,Notice,StudentLeave,TeacherLeave

# Register your models here.
@admin.register(StudentInfo)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','dob','fatherName','fatherOccupation','motherName','motherOccupation','address','city','state','mobileNo')


@admin.register(Staffs)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','dob','subject','qualification','experience','mobileNo')

admin.site.register(Assignment)
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','name','designation','feedback')

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','title','date','notice')

@admin.register(StudentLeave)
class StudentLeaveAdmin(admin.ModelAdmin):
    list_display = ('name','date','days','leaveReason')

@admin.register(TeacherLeave)
class TeacherLeaveAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','date','days','leaveReason')
