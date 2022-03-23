from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.shortcuts import redirect
from .models import Data
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.user.is_authenticated:
        return render(request,'success.html') 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
        
        if user is not None:
            login(request,user)
            return render(request,'success.html')
        else:
            form = AuthenticationForm()
            return render(request,'login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout(request):
    pass

@login_required(login_url ='login.html')
def res_dash(request):
    #calculate parameters
    context = {
        

    }
    return render(request, 'res_dash.html',context)
    pass

@login_required(login_url ='login.html')
def soc_dash(request):
    context = {

    }
    return render(request, 'soc_dash.html',context)

def data_enter(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        soc_id = body.get('Systerm ID')
        if Society.objects.filter(society_id = soc_id).exists():
            n_houses = body.get('Totalhouse data taken')
            houses = body.get('houseID')
            g_r = body.get('GreenWasteReading')
            b_r = body.get('BlueWasteReading')
            r_r = body.get('RedWasteReading')
            for i in range(n_houses):
                d = Data(house_id = houses[i], soc_id = t_id, b_1 = g_r[i], b_2 = b_r[i], b_3 = r_r[i])
                d.save()
            return JsonResponse({"data_stored": "OK"})
    else:
        return redirect(home)