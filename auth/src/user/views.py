from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import Registration, Login
from django.contrib.auth.decorators import login_required
def register(request):
    form = Registration(request.POST or None)
    context = {
        'form': form
    }
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            form.save()
            auth_user = authenticate(username= form.cleaned_data.get('username'), password=password)
            return redirect('users:login')
    return render(request, 'register.html', context)


def login_view(request):
    new = request.GET.get('next') 
    form = Login(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            auth_user = authenticate(username = username, password=password)
            login(request,auth_user)
            if new:
                return redirect(new)
            else:
                return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required
def premium_view(request):
    return render(request,'premium.html',{})



