from django.shortcuts import render

from catalog.models import Category


def base(request):
    product_list = Category.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, "catalog/category.html", context)
