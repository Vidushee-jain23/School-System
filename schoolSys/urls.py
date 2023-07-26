"""
URL configuration for schoolSys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('admin_sign_up/', include('principal.urls')), 
    path('admin_login/',include('principal.urls')),
    path('head/',include('principal.urls')),
    path('admin_logout/', include('principal.urls')),
    path('register/', include('principal.urls')),
    path('admit/', include('principal.urls')),
    path('staffform/', include('principal.urls')),
    path('staffdata/', include('principal.urls')),
    path('adminchngpass/', include('principal.urls')),
    path('studchngpass/', include('principal.urls')),
    path('staffchngpass/', include('principal.urls')),
    path('student_sign_up/', include('principal.urls')),     
    path('student_login/',include('principal.urls')), 
    path('student_logout/', include('principal.urls')),
    path('student/',include('principal.urls')),
    path('teacher_sign_up/', include('principal.urls')), 
    path('teacher_login/',include('principal.urls')),
    path('teacher/',include('principal.urls')),
    path('teacher_logout/', include('principal.urls')),
    path('assign/', include('principal.urls')),
    path('feed/', include('principal.urls')),
    path('notice/', include('principal.urls')),
    path('showfeed/', include('principal.urls')),
    path('shownotice/', include('principal.urls')),
    path('showassign/', include('principal.urls')),
    path('studleave/', include('principal.urls')),
    path('staffleave/', include('principal.urls')),
    path('showstudleave/', include('principal.urls')),
    path('showstaffleave/', include('principal.urls')),
]
