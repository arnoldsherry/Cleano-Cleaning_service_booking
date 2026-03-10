from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('companyhome/',views.companyhome,name='companyhome'),
    path('companyprofile/',views.companyprofile,name='companyprofile'),
    path('changepassword/',views.company_changepassword,name='company_changepassword'),
    path('service/',views.service,name='service'),
    path('add_service/',views.add_service,name='add_service'),
    path('viewservices/',views.viewservices,name='viewservices'),
    path('editservice/<int:sid>',views.editservice,name='editservice'),
    path('deleteservice/<int:sid>',views.deleteservice,name='deleteservice'),
    path('viewbookingrequests/',views.viewbookingrequests,name='viewbookingrequests'),
    path('acceptbooking/<int:bookingid>',views.acceptbooking,name='acceptbooking'),
    path('rejectbooking/<int:bookingid>',views.rejectbooking,name='rejectbooking'),
    path('deletebooking/<int:bookingid>',views.deletebooking,name='deletebooking'),
    path('reportcategorycount/',views.reportcategorycount,name='reportcategorycount'),
    path('company_logout/',views.company_logout,name='company_logout'),
    path('companyprofile/',views.companyprofile,name='companyprofile'),
    path('company_changepassword/',views.company_changepassword,name='company_changepassword'),
    path('company_editprofilepage/',views.company_editprofilepagepage,name='company_editprofilepage'),
    path('company_editprofile/',views.company_editprofile,name='company_editprofile'),
    path('filllocation/',views.filllocation,name='filllocation'),
    path('reportservicecount/',views.reportservicecount,name='reportservicecount'),
]