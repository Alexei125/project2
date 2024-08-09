from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/category/html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_list.html"


class MyView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"


def form_valid(self, form):
    product = form.save()
    user = self.request.user
    product.owner = user
    user.save()
    return super().form_valid(form)
