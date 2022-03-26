from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
# from .models import CustomUser,Society,Data

# def home(request):
#     if request.method == "POST":
#         if request.user.is_athenticated():
#             return render(request, "user/home.html")

#     return render(request, "landing/home.html")

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "user/signup.html"

# # class UserLoginView(CreateView):
# #     form_class = LoginForm
# #     # success_url = reverse_lazy("login")
# #     template_name = "user/login.html"

# def user_login(request):
#     if request.method == "POST":
#         fm = AuthenticationForm(request=request, data=request.POST)
#         if fm.is_valid():
#             uname = fm.cleaned_data['username']
#             pwd = fm.cleaned_data['password']
#             user = authenticate(username=uname, password=pwd)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/aruneo/')
#     else:
#         fm = AuthenticationForm()
#     return render(request, "user/login.html", {"form": fm})

# def user_logout(request):
#     logout(request)
#     return render(request, "user/logout.html")

# @login_required
# def user_dash(request):
#     if request.user.is_authenticated:
#         user = request.user
#         loaded_user = CustomUser.objects.filter(username=user.username)
#         cnt ={
#             "user_info": {
#                 "uid": loaded_user.user_id,
#                 "uname": loaded_user.username,
#                 "ufname": loaded_user.first_name,
#                 "ulname": loaded_user.last_name,
#                 "is_sec": is_secratry(loaded_user),
#             }
#         }
#         return render(request, "user/dashboard/userdash.html")

# @csrf_exempt
# def data_enter(request):
#     if request.method == "POST":
#         pass
#     else:
#         return HttpResponse()

# def is_secratry(user):
#     return user.groups.filter(name="Secretary").exists()