from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from datetime import datetime

class CustomUser(AbstractUser):
    house_id  = models.IntegerField(unique=True,null=True)
    user_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    soc_id = models.IntegerField(default=0,null=True)
    # username = models.CharField(max_length=50, unique=True)
    fun = models.CharField(max_length=50, default ="delete this")
    def __str__(self):
        return self.username

class Society(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, default="Please Enter Address")
    transmitter_id = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Data(models.Model):
    # data_id must be an auto generated number
    soc_id = models.ForeignKey(Society,default ='', on_delete=models.CASCADE)
    date = models.DateField(blank=True,null=True)
    user_associated = models.ForeignKey(CustomUser,default='', on_delete=models.CASCADE)
    work =models.CharField(max_length=50,default="hello")
    bucket_1 = models.IntegerField(default=0)
    bucket_2 = models.IntegerField(default=0)
    bucket_3 = models.IntegerField(default=0)

    def __str__(self):
        return self.data_id + " " + self.soc_id.name + " " + self.date.strftime("%Y-%m-%d")
    
    def generate_data_id():
        return self.date+" "+self.soc_id+" "+self.user_assocaited