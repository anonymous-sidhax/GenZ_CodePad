from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return render(request, "index.html")