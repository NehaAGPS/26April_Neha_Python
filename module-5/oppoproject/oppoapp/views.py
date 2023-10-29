from django.shortcuts import render
from .form import product_form
from .models import addproduct,productaddreal
# Create your views here.

def index(request):
    
    return render(request,'index.html')

def oderadd(request):
    if request.method=='POST':
        user=product_form(request.POST)
        if user.is_valid():
            user.save()
            print("your acount crt")
        else:
            print(user.errors)
    return render(request,'orderadd.html')

def addproducts(request):
    if request.method=='POST':
        user=product_form(request.POST)
        if user.is_valid():
            user.save()
            print("your acount crt")
        else:
            print(user.errors)
    return render(request,'addproduct.html')