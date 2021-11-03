from django.shortcuts import render

def index(request):
    while(1):
        return render(request, "index.html", {
            'code': 'Printing Text to Speech Output here',
        })
    return render(request, "index.html")
    
def about_us(request):
    return render(request, "about_us.html")