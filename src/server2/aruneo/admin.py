from django.contrib import admin
from .models import CustomUser, Data, House, Society
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Data)
admin.site.register(House)
admin.site.register(Society)