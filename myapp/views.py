from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from .models import RequestBlood,BloodGroup

# Create your views here.
def home(request):
    return render(request,'home.html')





def see_all_request(request):
    requests = RequestBlood.objects.all()
    return render(request, "all_request.html", {'requests':requests}) 


def request_blood(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        pincode = request.POST['pincode']
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        blood_requests = RequestBlood(name=name, email=email, phone=phone,pincode=pincode, blood_group=BloodGroup.objects.get(name=blood_group), date=date)
        blood_requests.save()
        return render(request, "base.html")     
    return render(request, "request_blood.html")       




def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
            return redirect('/')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return redirect('/')




def user_logout(request):
    logout(request)
    return redirect('/')