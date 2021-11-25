from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import events


# Create your views here.
def watch(request):
    obj1=events.objects.all()
    return render(request,"index.html",{'event':obj1})

def fun(request):
    obj=place.objects.all()
    return render(request,"index.html",{'places':obj})

def add(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{'add':num3})    
