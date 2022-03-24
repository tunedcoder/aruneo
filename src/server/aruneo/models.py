from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    house_id  = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    # username = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.username

class Society(models.Model):
    name = models.CharField(max_length=50)
    transmitter_id = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Data(models.Model):
    #data_id must be an auto generated number
    soc_id = models.ForeignKey(Society, on_delete=models.CASCADE)
    date = models.DateField()
    user_associated = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    bucket_1 = models.IntegerField(default=0)
    bucket_2 = models.IntegerField(default=0)
    bucket_3 = models.IntegerField(default=0)

    def __str__(self):
        return self.data_id + " " + self.soc_id.name + " " + self.date.strftime("%Y-%m-%d")
    
    def generate_data_id():
        return self.date+" "+self.soc_id+" "+self.user_assocaited