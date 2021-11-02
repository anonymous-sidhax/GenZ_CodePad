from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
    
def about_us(request):
    return render(request, "about_us.html")
