from django.shortcuts import render

from catalog.models import Product


def base(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, "catalog/category.html", context)


def products(request, pk):
    product = get_objects_or_404(Product, pk=pk)
    context = {'product': product}
    return (request, "catalog/product.html", context)