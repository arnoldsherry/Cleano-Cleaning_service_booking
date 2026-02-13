from django.db import models
from adminapp.models import tbl_category
from guestapp.models import tbl_login, tbl_company,user
from companyapp.models import tbl_service
# Create your models here.
class tbl_booking(models.Model):
    bookingid=models.AutoField(primary_key=True)
    serviceid=models.ForeignKey('companyapp.tbl_service',on_delete=models.CASCADE)
    bookingstatus=models.CharField(max_length=50)
    userid=models.ForeignKey('guestapp.user',on_delete=models.CASCADE)
    bookingdate=models.DateField()
class tbl_payment(models.Model):
    paymentid=models.AutoField(primary_key=True)
    bookingid=models.ForeignKey('userapp.tbl_booking',on_delete=models.CASCADE)
    paymentdate=models.DateField()
    totalamount=models.IntegerField()
    paymentstatus=models.CharField(max_length=50)