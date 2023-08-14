from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order , OrderItem

def say_hello(request):
    queryset = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    result_count = queryset.count()
    return render(request, 'hello.html', {'name': 'erfan', 'orders': list(queryset), 'result_count': result_count})