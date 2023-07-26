from collections import namedtuple
from django.urls import path
from . import views, studentviews, teacherviews

urlpatterns = [
    path('home/', views.home_view, name="home"),
    path('admin/', views.admin_sign_up, name="admin_sign_up"),
    path('adminlogin/', views.admin_user_login, name="admin_login"),
    path('head/', views.head, name="head"),
    path('logout/', views.admin_logout, name="admin_logout"),
    path('register/', views.showformdata, name="register"),
    path('admit/', views.showdata, name="admit"),
    path('staffform/', views.staff_showformdata, name="staffform"),
    path('staffdata/', views.staff_showdata, name="staffdata"),
    path('notice/', views.create_notice, name="notice"),
    path('showfeed/', views.show_feed, name="showfeed"),
    path('showstaffleave/', views.show_teaLeave, name="showstaffleave"),
    path('delete/<int:id>/',views.delete_data, name = "deletedata"),
    path('<int:id>/',views.update_data, name = "updatedata"),
    path('adminchngpass/', views.admin_change_pass, name="adminchngpass"),
    path('deletestaff/<int:id>/',views.delete_data_staff, name = "deletestaff"),
    path('updatestaff/<int:id>/',views.update_data_staff, name = "updatestaff"),


    #student
    path('student/', studentviews.student_sign_up, name="student_sign_up"),
    path('studentlogin/', studentviews.student_user_login, name="student_login"),
    path('studenthome/', studentviews.student_view, name="studenthome"),
    path('studentlogout/', studentviews.student_logout, name="student_logout"),
    path('feed/', studentviews.create_feed, name="feed"),
    path('shownotice/', studentviews.show_notice, name="shownotice"),
    path('showassign/', studentviews.show_assignment, name="showassign"),
    path('studleave/', studentviews.leave_requeststu, name="studleave"),
    path('studchngpass/', studentviews.stud_change_pass, name="studchngpass"),
    

    #teacher
    path('teacher/', teacherviews.teacher_sign_up, name="teacher_sign_up"),
    path('teacherlogin/', teacherviews.teacher_user_login, name="teacher_login"),
    path('teacherhome/', teacherviews.teacher_home, name="teacherhome"),
    path('teacherlogout/', teacherviews.teacher_logout, name="teacher_logout"),
    path('assign/', teacherviews.assign_student, name="assign"),
    path('staffleave/', teacherviews.leave_request, name="staffleave"),
    path('showstudleave/', teacherviews.show_studLeave, name="showstudleave"),
    path('staffchngpass/', teacherviews.staff_change_pass, name="staffchngpass"),
]