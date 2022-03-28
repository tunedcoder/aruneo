from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomChangeForm
from .models import CustomUser,Society,Data

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ["username","user_id"]

    # list_display = ('email', 'date_of_birth', 'is_admin')
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        ('Personal info', {'fields': ('first_name','last_name','user_id')}),
        # ('Permissions', {'fields': ('is_admin',)}),
        ('Data Collection', {'fields': ('soc_id','house_id')}),
    )


class SocietyAdmin(admin.ModelAdmin):
    model =Society
    list_display = ["name","transmitter_id"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Society, SocietyAdmin)
admin.site.register(Data)