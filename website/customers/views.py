from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages 
from . models import customers

# Create your views here.

def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:

            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
            #create user account

            user = User.objects.create_user(
                username = username,
                password  = password,
                email = email
            )

            #create customer account

            customer = customers.objects.create(
                user = user,
                phone = phone,
                address = address
            )
            success_msg = "Registration completed successfully"
            messages.success(request,success_msg)
        except Exception as e:
            error_msg = "Duplicate username or Invalid inputs"
            messages.error(request,error_msg)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid user credentials')
    return render(request,'account.html',context)

def log_out(request):
    logout(request)
    return redirect('home')