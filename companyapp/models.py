from django.db import models
from guestapp.models import tbl_company
from adminapp.models import tbl_category
# Create your models here.
class tbl_service(models.Model):
    serviceid=models.AutoField(primary_key=True)
    servicename=models.CharField(max_length=100)
    totalamount=models.BigIntegerField()
    image=models.ImageField()
    description=models.CharField(max_length=100)
    compid=models.ForeignKey('guestapp.tbl_company',on_delete=models.CASCADE)
    categoryid=models.ForeignKey('adminapp.tbl_category',on_delete=models.CASCADE)