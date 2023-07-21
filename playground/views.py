from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    
    #1: exists = Product.objects.filter(pk=0).exists()
    
    #2 try:
    #     product = Product.objects.get(pk=0)
    # except:
    #     pass
    
    #3 product = Product.objects.filter(pk=0).first()
    
    return render(request,'hello.html',{'name':'erfan'})