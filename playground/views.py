from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
    # keyword=value
    #select_related (1)
    # prf
    queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

    return render(request, 'hello.html', {'name':'Reuf', 'products': queryset})

