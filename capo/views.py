from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Guitar,  Accessories,  Apparel


# Create your views here.


def Index(request):
    return render (request, 'Index.html')


def Guitars(request):
    
    guitar = Guitar.objects.all()

    context={
        'guitar' : guitar,
       
    }
    return render(request, "Guitars.html", context)

def Accessoriess(request):
    access = Accessories.objects.all()  

    context={
        'access' : access,
       
    }
    return render(request, "Accessories.html", context)

def Apparels(request):
    appa = Apparel.objects.all()  

    context={
        'appa' : appa,
       
    }
    return render(request, "Apparel.html", context)