from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import *
from django.db.models import Q, F , Value
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order , OrderItem , Customer

def say_hello(request):
    queryset = Customer.objects.annotate(new_id = F('id') + 1)
    return render(request, 'hello.html', {'name': 'erfan', 'queryset': list(queryset)})