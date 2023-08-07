from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

def say_hello(request):
    last_order = OrderItem.objects.values_list('order__customer__first_name','product__title','order__placed_at').order_by('-order__placed_at')[:7]
    result_count = last_order.count()
    return render(request, 'hello.html', {'name': 'erfan', 'orders': last_order, 'result_count': result_count})
