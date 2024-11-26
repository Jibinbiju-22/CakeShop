from django.db import models

# Create your models here.


class tbllogin(models.Model):
    loginid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
