from django.shortcuts import render
from Bloodbook.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from .models import UserProfileInfo

def index(request):
    return render(request,'Bloodbook/index.html')
def about(request):
    return render(request,'Bloodbook/aboutus.html')
def search(request):
    Webpages_list = UserProfileInfo.objects.order_by('state')
    state_dict = {'User_info':Webpages_list}
    return render(request,'Bloodbook/search.html',context = state_dict)
@login_required
def special(request):
    return HttpResponse("You are logged in!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'Bloodbook/registration.html',
                                {'user_form':user_form,
                                 'profile_form':profile_form,
                                 'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone else tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login details!")
    else:
        return render(request,'Bloodbook/login.html',{})
