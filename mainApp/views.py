from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def homePageView(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    # form = UserCreationForm()

    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         return redirect('login')
    
    # return render(request, 'register.html', {'form': form})
    return render(request, "register.html")

def forget_password(request):
    return render(request, "forget_password.html")