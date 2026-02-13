from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('searchservice/',views.searchservice,name='searchservice'),
    path('fillservices/',views.fillservices,name='fillservices'),
    path('servicepage/<int:serviceid>/',views.servicepage,name='servicepage'),
    path('bookservice/',views.bookservice,name='bookservice'),
    path('mybookings/',views.mybookings,name='mybookings'),
    path('paymentpage/<int:bookingid>/',views.paymentpage,name='paymentpage'),
    path('cancelbooking/<int:bookingid>/',views.cancelbooking,name='cancelbooking'),
    path('deletebooking/<int:bookingid>/',views.deletebooking,name='deletebooking'),
    path('pay/',views.pay,name='pay'),
    path('viewpaidservices/',views.viewpaidservices,name='viewpaidservices'),
]