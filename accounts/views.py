# from audioop import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm, UserForm, ProfileForm, LoginForm
from .models import Profile
# from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == 'post':
        form = SignupForm(request.post, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('jobs')
        else :
            print(form.errors)
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form':form})



def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'post':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request, 'profile_edit.html', {'userform':userform, 'profileform':profileform})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})





