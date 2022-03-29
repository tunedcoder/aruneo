from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CustomUser,Society,Data

def home(request):
    if request.user.is_authenticated:
        return render(request, "user/dash.html")

    return render(request, "landing/home.html")

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "user/signup.html"

# class UserLoginView(CreateView):
#     form_class = LoginForm
#     # success_url = reverse_lazy("login")
#     template_name = "user/login.html"

def user_login(request):
    # if request.user.is_athenticated():
    #     return render(request, "user/dash.html")
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
    return render(request, "user/logout.html")

@login_required
def user_dash(request):
    if request.user.is_authenticated:
        user = request.user
        loaded_user = CustomUser.objects.get(username=user.username)
        garbage_data = Data.objects.get(user_associated=loaded_user.user_id)
        cnt ={
            "user_info": {
                "uid": loaded_user.user_id,
                "uname": loaded_user.username,
                "ufname": loaded_user.first_name,
                "ulname": loaded_user.last_name,
                "is_sec": is_secratry(loaded_user),
                "g_data": garbage_data,
            }
        }

        garbage_data = Data.objects.get(user_id=loaded_user.user_id)

        return render(request, "user/dash.html",{"cnt":cnt})

@csrf_exempt
def data_enter(request):
    if request.method == "POST":
        if Society.objects.filter(transmitter_id=request["System ID"]).exists():
            society = Society.objects.get(transmitter_id=request["System ID"])
            so_id = society.society_id
            Houses = request["houseID"]
            for i in range(len(Houses)):
                g_r = request["GreenWasteReading"][i]
                b_r = request["BlueWasteReading"][i]
                r_r = request["RedWasteReading"][i]
                d_id = datetime.date.today().strftime("%d%m%Y")+""+soc_id+""+Houses[i]
                u_associated = CustomUser.objects.get(soc_id=so_id,house_id=Houses[i])
                d = Data(data_id = d_id,date=datetime.date.today(), user_associated=u_associated.user_id,soc_id=so_id,house_id=Houses[i],green_waste_reading=g_r,blue_waste_reading=b_r,red_waste_reading=r_r)
                d.save()
    else:
        return HttpResponse()

def is_secratry(user):
    return user.groups.filter(name="Secretary").exists()