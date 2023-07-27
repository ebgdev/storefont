from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    product = Product.objects.latest('unit_price')
    return render(request,'hello.html',{'name':'erfan','product': product})
