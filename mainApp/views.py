from django.shortcuts import render

import sys

# def index(request):
#     while(1):
#         return render(request, "index.html", {
#             'code': 'Printing Text to Speech Output here',
#         })
#     return render(request, "index.html")

def index(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about_us.html")

def sst(request):
    print("Inside FUnction")
    return render(request, "about_us.html")
    
def runcode(request):

    if request.method == "POST":
        code = request.POST['codearea']

        try:

            original_stdout = sys.stdout
            sys.stdout = open('output_files\\file.txt', 'w')

            # Execute Code
            exec(code)

            sys.stdout.close()

            # Reset the standard output to its original value
            sys.stdout = original_stdout

            # Read output from file and save in output variable
            output = open('output_files\\file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e

    # Return and render index page and send codedata and output to show on page
    return render(request , 'index.html', {"code":code , "output":output})