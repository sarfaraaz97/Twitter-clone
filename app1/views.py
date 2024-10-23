from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app1.models import tweet
# Create your views here.

def homeView(request):
    obj=tweet.objects.all()
    return render(request,'home.html',{'result':obj})

def loginView(request):
    if request.user.is_authenticated:
        messages.error(request,'YOU LOGGED IN...')
        return redirect('home_page')
    if request.method=="POST":
        usrnm=request.POST.get('lion')
        passw=request.POST.get('elephant')
        print(usrnm)
        print(passw)
        result=authenticate(request,username=usrnm,password=passw)
        if result:
            login(request,result)
            messages.success(request,"Successfully logged in")
            return redirect('profile_page')
        else:
            messages.error(request,"WRONG PASSWORD OR USERNAME")
            return render(request,'login.html')
    return render(request,'login.html')
       

@login_required(login_url='login_page')
def profileView(request):
    if request.user.is_superuser:
        print(request.user.username)
        return redirect('admin/')
    return render(request,'profile.html')

def logoutView(request):
    logout(request)
    messages.error(request,"PLEASE LOGIN")
    return redirect('home_page')

def registerView(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        print(uname,fname,lname,email,passw,cpass)
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Please use another username!")
            return redirect('register_page')
        if len(passw)<8:
            messages.error(request,'password must contain 8 characters')
            return redirect('register_page')
        if (cpass!=passw):
            messages.error(request,"password doesnot match")
            return redirect('register_page')
        obj=User(username=uname,first_name=fname,last_name=lname,email=email)
        obj.set_password(passw)
        obj.save()
        messages.success(request,"Hey successfully registered")
        return redirect('login_page')
    return render(request,'register.html')

@login_required(login_url='login_page')
def tweetView(request):
    if request.method=="POST":
        post=request.POST.get('post')
        uname=request.user.username
        obj=tweet(uname=uname,post=post)
        obj.save()
    return render(request,'tweet.html')

@login_required(login_url='login_page')
def deleteView(request,rid):
    if request.user.is_superuser:
        obj=tweet.objects.get(id=rid)
        obj.delete()
        messages.success(request,"Deleted Successfully")
        return redirect('home_page')
    else:
        messages.warning(request,"user cannot delete")
        return redirect('home_page')


def display(request,rid):
    b=tweet.objects.get(id=rid)
    if request.method=="POST":
        b.post=request.POST.get('desc')
        b.save()
    return render(request,'single.html',{'res':b})


