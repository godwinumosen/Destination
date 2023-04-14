from django.shortcuts import render,redirect
from .models import ProductDestination

# Create your views here.

def home (request):
    dests = ProductDestination.objects.all()
    context = {
        'dests':dests
    }
    return render(request,'index.html',context)

    
def register(request):
    return render(request, 'register.html')
