from django.core.management.base import BaseCommand
# from django_faker import Faker
import random
import numpy as np
import datetime
# fake = Faker()

from aruneo.models import Data,CustomUser,Society

weights = np.random.randint(500,2500,size=(7,120,3))

weights_kg = np.array([x/1000 for x in weights])
print(weights_kg[0].shape)
date_starts = datetime.date.today() - datetime.timedelta(days=120)

class Command(BaseCommand):
    help = "Command information"

    def handle(self,*args,**kwargs):
        users=CustomUser.objects.all()
        for i,u in enumerate(users):
            soc_id = Society.objects.get(name=u.soc_name)
            u_associated = u
            for day in range(120):
                date = date_starts + datetime.timedelta(days=day)
                d_id = str(date)+"_"+str(soc_id)+"_"+str(u_associated)
                d = Data(data_id = d_id,soc_id=soc_id,date=date,user_associated=u_associated,bucket_1=weights_kg[i][day][0],bucket_2=weights_kg[i][day][1],bucket_3=weights_kg[i][day][2])
                d.save()
                print(d.data_id)