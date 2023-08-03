from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

def say_hello(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset_titles = queryset.keys()
    result_count = queryset.count()
    return render(request, 'hello.html', {'name': 'erfan', 'products': queryset, 'result_count': result_count})
