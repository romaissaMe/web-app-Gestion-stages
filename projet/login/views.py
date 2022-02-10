from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user (request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,("Une erreue d'authentification veuillez essayer une autre fois"))
            return redirect('login')    
    elif request.method=='GET':
       return render(request,'authentification/log_in.html',{})

def logout_user(request):
    messages.success(request,("tu as deconnecte !"))
    return redirect('login')

def register (request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Compte Cree !"))
            return redirect('home')
    else:
        form=UserCreationForm()        
    return render(request,'authentification/register.html',{'form':form})
   
