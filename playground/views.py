from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    queryset = Product.objects.values('id','title','collection__title').order_by('id')
    return render(request,'hello.html',{'name':'erfan','products': queryset})