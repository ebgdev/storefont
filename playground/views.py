from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import *
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order , OrderItem

def say_hello(request):
    result = Product.objects.aggregate(we_can_say = Count('id'),min_price = Min('unit_price'))
    return render(request, 'hello.html', {'name': 'erfan', 'result': result})