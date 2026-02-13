from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('guesthome/',views.guesthome),
    path('customer/',views.customer,name='customer'),
    path('customerreg/',views.customerreg,name='customerreg'),
    path('viewcustomer/',views.viewcustomer,name='viewcustomer'),
    path('editcustomer/<customerid>',views.editcustomer,name='editcustomer'),
    path('deletecustomer/<customerid>',views.deletecustomer,name='deletecustomer'),
    path('company/',views.company,name='company'),
    path('companyreg/',views.companyreg,name='companyreg'),
    path('login/',views.login,name='login'),
    path('login_insert/',views.login_insert,name='login_insert'),
]