from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

def say_hello(request):
    #we do also have defer method to select all fields except one 
    queryset = Product.objects.only('id','title')
    # queryset_titles = queryset.keys()
    result_count = queryset.count()
    return render(request, 'hello.html', {'name': 'erfan', 'products': queryset, 'result_count': result_count})
