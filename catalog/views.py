from django.shortcuts import render

from catalog.models import Product


def base(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, "catalog/base.html", context)
