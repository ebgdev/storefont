from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import *
from django.db.models import Q, F , Value , Func
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order , OrderItem , Customer

def say_hello(request):
    queryset = Customer.objects.annotate(full_name = Concat('first_name',Value(' '),'last_name'))
    result_count = queryset.count()
    return render(request, 'hello.html', {'name': 'erfan','result_count':result_count ,'queryset': list(queryset)})