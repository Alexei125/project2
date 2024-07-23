from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/category/html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_list.html"

# def products(request, pk):
# product = get_objects_or_404(Product, pk=pk)
# context = {'product': product}
# return (request, "catalog/product_list.html", context)
