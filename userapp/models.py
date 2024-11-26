from django.db import models
from guestapp.models import *
import datetime
from adminapp.models import *

# Create your models here.


class tbluser(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    contactnumber = models.BigIntegerField()
    password = models.CharField(max_length=50)
    profilephoto = models.ImageField()
    loginid = models.ForeignKey(tbllogin, on_delete=models.CASCADE,default="")


class tblbooking(models.Model):
    bookingid = models.AutoField(primary_key=True)
    deliveryaddress = models.CharField(max_length=500)
    requireddate = models.DateField()
    quantity = models.IntegerField(max_length=50)
    totalamount = models.IntegerField(max_length=50)
    bookingdate = models.DateField(default=datetime.date.today())
    bookingstatus = models.CharField(max_length=50)
    cakeid = models.ForeignKey(tblcake, on_delete=models.CASCADE, default="")
    loginid = models.ForeignKey(tbllogin, on_delete=models.CASCADE, default="")