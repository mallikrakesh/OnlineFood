from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,'myadmin/index.html')