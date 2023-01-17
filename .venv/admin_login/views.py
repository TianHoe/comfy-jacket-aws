from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpass = request.POST['confpass']

        if password == confirmpass:
            if User.objects.filter(username=username).exists():
                print('Username existed! Try another name.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('Email is already taken!Try another one.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            print('Your Password did not matched!')
            return redirect('register')
    else:
        return render(request, 'adminlogin/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login successful')
            return redirect('showBouquets')
        else:
            print('Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'adminlogin/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from site...')
        return redirect('login')
    return redirect('login')