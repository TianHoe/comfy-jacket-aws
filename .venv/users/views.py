from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ProfileForm, EditProfileform, ChangePWform
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, '.')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            subject = 'Welcome to Banana Florist!'
            message = f'Hi {user.username}, thank you for registering in Banana Florist.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('home')
    else:
        form = SignupForm()
        
    context = { 'form': form }
    return render(request, 'signup.html', context)

def logout_user(request):
    logout(request)
    
    return render(request, 'logout.html', {})

# USER PROFILE
def profile(request):
    if request.method == 'POST':
        form = EditProfileform(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(commit=False)
            if form.cleaned_data.get("remove") == True:
                custom_form.profile_img = ""
            custom_form.user = user_form
            custom_form.save()
            return redirect('/profile/')
    else:
        form = EditProfileform(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = { 
            'form': form,
            'profile_form': profile_form,
            'img': request.user.profile.profile_img
        }
        return render(request, 'editprofile.html', context)

def view_profile(request):
    object = request.user
    profile_obj = request.user.profile
    context = { 
        'object': object,
        'profile_obj': profile_obj,
    }
    return render(request, 'profile.html', context)



def change_pw_view (request):
    my_user = request.user
    if request.method == 'POST':
        form = ChangePWform(data=request.POST, user=my_user)

        if form.is_valid():
            form.save()
            try:
                del request.session['change_error']
                return redirect('/logout/')
            except:
                return redirect('/logout/')
        else:
            request.session['change_error'] = True
            return redirect('/profile/edit/pw')
    else:
        form = ChangePWform(user=my_user)
        
        try:
            pw_error = request.session['change_error']
        except:
            pw_error = False
        context = { 
            'form': form,
            'pw_error': pw_error
        }
        return render(request, 'editpwprofile.html', context)