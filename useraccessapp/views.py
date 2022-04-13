from django.shortcuts import render,redirect
from .forms import RegisterUserForm,Userinfoform
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def home(request):
    return render(request,'useraccessapp/index.html')  






def register(request):
    
    form = RegisterUserForm
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('signin') 
    
    context ={'form':form}
    return render(request,'useraccessapp/register.html', context)


def signin(request):
       if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
       
          user = authenticate(request, username=username, password=password)
          
          if user is not None:
            login(request, user)
            return redirect('profile')
          else: 
             messages.info(request, 'Username OR password is incorrect') 

       context = {}        
       return render(request,'useraccessapp/signin.html',context)


@login_required(login_url='signin')
def profile(request):
    return render(request,'useraccessapp/profile.html')


def signout(request):
        logout(request)
        return redirect ('signin')
    
    
def update(request):
  
    profile = request.user.profile
    form = Userinfoform(instance=profile)
    if request.method == 'POST':
       form = Userinfoform(request.POST, request.FILES, instance=profile)
       if form.is_valid():
          form.save()    
    
    context = {'form':form}
    return render (request, 'useraccessapp/update.html',context)