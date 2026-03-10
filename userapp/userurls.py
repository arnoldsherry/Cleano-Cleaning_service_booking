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
    path('reportcategorycount/',views.reportcategorycount,name='reportcategorycount'),
    path('addcleanocredit/',views.addcleanocredit,name='addcleanocredit'),
    path('add_credit/',views.add_credit,name='add_credit'),
    path('paywithcreditbalance/<int:bookingid>/',views.paywithcreditbalance,name='paywithcreditbalance'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('reportservicecount/',views.reportservicecount,name='reportservicecount'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('editprofilepage/',views.editprofilepage,name='editprofilepage'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('filllocation/',views.filllocation,name='filllocation'),
    path('fillservicesbycompany/',views.fillservicesbycompany,name='fillservicesbycompany'),
    path('searchservicesbycompany/',views.searchservicesbycompany,name='searchservicesbycompany'),
]