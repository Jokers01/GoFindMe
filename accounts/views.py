from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm , ProfileForm, UserForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.db import transaction

def home(request):
    return render(request,"home.html")

def homeawal(request):
    return render(request,"homeawal.html")

def signup(request):
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('home')
        else:
            form = SignUpForm()
        return render(request,'signup.html',{'form':form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('my_account')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'my_account.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
