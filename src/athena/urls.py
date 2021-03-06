"""Athena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from user.views import (
        EmployeeDetailView, EmployeeUpdateView, ProfileRedirectView, 
        EmergencyContactDeleteView, EmergencyContactCreateView, SalaryListView, 
        EmployeeListView, DepartmentListView, DesignationListView, 
        VacationListView, VacationCreateView, VacationDeleteView, VacationUpdateView,
    )

from django.conf.urls import (
    handler404, handler500
)

from vacations.views import HolidayListView, HolidayCreateView, HolidayDeleteView

from django.contrib import admin
from django.urls import re_path
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView

handler404 = 'user.views.handler404'
handler500 = 'user.views.handler500'

urlpatterns = [
    re_path(r'^login', LoginView.as_view(), name='login'),
    re_path(r'^logout', LogoutView.as_view(), name='logout'),
    re_path(r'^update-profile', EmployeeUpdateView.as_view(), name='update-profile'),
    re_path(r'^create-holiday', HolidayCreateView.as_view(), name='create-holiday'),
    re_path(r'^delete-holiday/(?P<holiday>[0-9]+)', HolidayDeleteView.as_view(), name='delete-holiday'),
    re_path(r'^create-emergency-contact', EmergencyContactCreateView.as_view(), name='create-emergency-contact'),
    re_path(r'^delete-contact/(?P<contact>[0-9]+)', EmergencyContactDeleteView.as_view(), name='delete-contact'),
    re_path(r'^employees', EmployeeListView.as_view(), name='employees'),
    re_path(r'^holidays', HolidayListView.as_view(), name='holidays'),
    re_path(r'^vacation', VacationListView.as_view(), name='vacation'),
    re_path(r'^create-vacation', VacationCreateView.as_view(), name='create-vacation'),
    re_path(r'^delete-vacation/(?P<vacation>[0-9]+)', VacationDeleteView.as_view(), name='delete-vacation'),
    re_path(r'^update-vacation/(?P<vacation>[0-9]+)', VacationUpdateView.as_view(), name='update-vacation'),
    re_path(r'^departments', DepartmentListView.as_view(), name='departments'),
    re_path(r'^designations', DesignationListView.as_view(), name='designations'),
    re_path(r'^salary', SalaryListView.as_view(), name='salary'),
    re_path(r'^admin', admin.site.urls, name='admin'),
    re_path(r'^profile/(?P<username>[\w-]+)', EmployeeDetailView.as_view(), name='home'),
    re_path(r'^', ProfileRedirectView.as_view(), name='redirect'),
]
