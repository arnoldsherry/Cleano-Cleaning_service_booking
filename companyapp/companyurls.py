from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('companyhome/',views.companyhome,name='companyhome'),
    path('service/',views.service,name='service'),
    path('add_service/',views.add_service,name='add_service'),
    path('viewservices/',views.viewservices,name='viewservices'),
    path('editservice/<int:sid>',views.editservice,name='editservice'),
    path('deleteservice/<int:sid>',views.deleteservice,name='deleteservice'),
    path('viewbookingrequests/',views.viewbookingrequests,name='viewbookingrequests'),
    path('acceptbooking/<int:bookingid>',views.acceptbooking,name='acceptbooking'),
    path('rejectbooking/<int:bookingid>',views.rejectbooking,name='rejectbooking'),
    path('deletebooking/<int:bookingid>',views.deletebooking,name='deletebooking'),
]