from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomChangeForm
from .models import CustomUser,Society,Data

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ["username","user_id","soc_name","house_id"]

    # list_display = ('email', 'date_of_birth', 'is_admin')
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        ('Personal info', {'fields': ('first_name','last_name','user_id')}),
        # ('Permissions', {'fields': ('is_admin',)}),
        ('Data Collection', {'fields': ('soc_name','house_id')}),
    )


class SocietyAdmin(admin.ModelAdmin):
    model =Society
    list_display = ["name","soc_id","transmitter_id"]

class DataAdmin(admin.ModelAdmin):
    model =Data
    list_display = ["data_id","soc_id"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Society, SocietyAdmin)
admin.site.register(Data,DataAdmin)