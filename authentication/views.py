from django.shortcuts import render

def login(request):
    return render(request=request, template_name="login.html")

def register(request):
    return render(request=request, template_name="register.html")

def forget_password(request):
    return render(request=request, template_name="forget_password.html")