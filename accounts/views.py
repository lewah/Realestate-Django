# from realestate import accounts
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
    
        if user is not None:   #AND
            auth.login(request,user)
            messages.success(request,'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request,'Wrong username or password')
            return redirect('login')
    
    else:
        return render(request,'accounts/login.html')
        # return render(request, 'accounts/login.html')

# def logout(request):
#     return render(request, 'accounts/logout.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are loged out')
        return redirect('homepage')  #index is the home page
    return redirect('homepage')

def register(request):
    if request.method == 'POST':   #if method is POST grab the data from the form  , ['name value of form from html']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name,last_name=last_name)
                    # auth.login(request, user)
                    user.save()
                    messages.success(request,'Registration successful')
                    return redirect('login')
        else:
            messages.error(request,'Passwords dont match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')