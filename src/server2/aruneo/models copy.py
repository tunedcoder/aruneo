from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    society_id = models.CharField(max_length=10, blank=True)
    house_id = models.CharField(max_length=10, blank=True)
    user_id = models.CharField(max_length=10, blank=True)
    is_secretary = models.BooleanField(default=False)


class Data(models.Model):
    data_id = models.CharField(max_length=100,auto_created=True)
    house_id = models.CharField(max_length=100)
    soc_id = models.CharField(max_length=100,blank=True)
    b_1 = models.FloatField()
    b_2 = models.FloatField()
    b_3 = models.FloatField()
    
    def __str__(self):
        return f'{self.data_id}_{self.soc_id}_{self.house_id}'

class House(models.Model):
    house_id = models.CharField(max_length=100)

class Society(models.Model):
    society_id = models.CharField(max_length=100)
    house_ids = models.ManyToManyField(House)

