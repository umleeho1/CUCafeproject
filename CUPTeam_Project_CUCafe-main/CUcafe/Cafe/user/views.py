from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from cafe import urls

# Create your views here.
def signup(request):
    if request.method=="GET":
        signupForm =UserCreationForm(request.GET)
        print(signupForm)
        context = {'signupForm':signupForm}
        return render(request, 'user/signup.html', context)
    elif request.method=="POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()
        return redirect('user:login')

def logout(request):
    auth_logout(request)
    return redirect('/board/list')

def login(request):
    if request.method=="GET":
        loginForm =AuthenticationForm()
        context = {'loginForm':loginForm}
        return render(request, 'user/login.html', context)
    elif request.method=="POST":
        loginForm = UserCreationForm(request, request.POST)
        if loginForm.is_valid():
           auth_login(request, loginForm.get_user())

        return redirect(request, 'board:main_index')