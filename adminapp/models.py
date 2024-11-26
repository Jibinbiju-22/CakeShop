from django.db import models

# Create your models here.


class tblcategory(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=50)
    categoryphoto = models.ImageField()


class tblflavour(models.Model):
    flavourid = models.AutoField(primary_key=True)
    flavourname = models.CharField(max_length=50)


class tblcake(models.Model):
    cakeid = models.AutoField(primary_key=True)
    cakename = models.CharField(max_length=50)
    cakedescription = models.CharField(max_length=500)
    cakeweight = models.IntegerField(max_length=50)
    amount = models.IntegerField(max_length=50)
    cakephoto = models.ImageField()
    categoryid = models.ForeignKey(tblcategory, on_delete=models.CASCADE, default="")
    flavourid = models.ForeignKey(tblflavour, on_delete=models.CASCADE, default="")
