from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
# from django.http import HttpResponse
# from django.db.models.aggregates import *
# from django.db.models import Q, F , Value , Func , ExpressionWrapper, DecimalField
# from django.db.models.functions import Concat
# from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order , OrderItem , Customer

def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)
    queryset = TaggedItem.objects \
        .select_related('tag') \
        .filter(
            content_type = content_type,
            object_id = 1,
        )
    return render(request, 'hello.html', {'name': 'erfan','tags': list(queryset)})  