from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # to order in 'x' prameter quote in prenteces like : order_by('x')
    queryset = Product.objects.all().order_by('unit_price')[::-1]

    return render(request,'hello.html',{'name':'erfan','products': list(queryset)})