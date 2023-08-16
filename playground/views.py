from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import *
from django.db.models import Q, F , Value , Func , ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order , OrderItem , Customer

def say_hello(request):
    # for monitoring values we should always use DeciamlField
    discounted_price =  ExpressionWrapper(F('unit_price') * 0.8 ,output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price =  discounted_price
    )
    result_count = queryset.count()
    return render(request, 'hello.html', {'name': 'erfan','result_count':result_count ,'queryset': list(queryset)})