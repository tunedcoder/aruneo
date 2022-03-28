from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name")

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        }