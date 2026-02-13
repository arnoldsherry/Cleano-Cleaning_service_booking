from django.db import models
from adminapp.models import tbl_location
# Create your models here.
class user(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    locationid=models.ForeignKey('adminapp.tbl_location', on_delete=models.CASCADE)
    contact=models.CharField(max_length=15)
    loginid=models.ForeignKey('tbl_login', on_delete=models.CASCADE)
    email=models.CharField(max_length=50)

class tbl_login(models.Model):
    loginid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="In Queue")
class tbl_company(models.Model):
    compid=models.AutoField(primary_key=True)
    compname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    locationid=models.ForeignKey('adminapp.tbl_location',on_delete=models.CASCADE)
    loginid=models.ForeignKey('tbl_login',on_delete=models.CASCADE)
    contact=models.CharField(max_length=11)
    city=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    image=models.ImageField()
    description=models.CharField(max_length=200)
    status=models.CharField(max_length=50,default="In Queue")
    