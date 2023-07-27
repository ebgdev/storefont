from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(unit_price__gte=90.02).order_by('title','unit_price')
    return render(request,'hello.html',{'name':'erfan','products': list(queryset)})
