from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

def home(request):
    if request.method == "POST":
        if request.user.is_athenticated():
            pass

    return render(request, "home.html")
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "user/signup.html"

# class UserLoginView(CreateView):
#     form_class = LoginForm
#     # success_url = reverse_lazy("login")
#     template_name = "user/login.html"

def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/aruneo/')
    else:
        fm = AuthenticationForm()
    return render(request, "user/login.html", {"form": fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/aruneo/')

def user_dash(request):
    pass

def soc_dash(request):
    pass

def data_enter(request):
    pass