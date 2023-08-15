from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import *
from django.db.models import Q, F , Value , Func
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order , OrderItem , Customer

def say_hello(request):
    queryset = Customer.objects.annotate(
        #CONCAT
        full_name = Func(F(('first_name')),Value(' '),F('last_name'),function = 'CONCAT')
    )
    result_count = queryset.count()
    return render(request, 'hello.html', {'name': 'erfan','result_count':result_count ,'queryset': list(queryset)})