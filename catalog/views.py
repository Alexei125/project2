from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/category/html"
    login_url = "/login/"
    redirect_field_name = "redirect_to"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_list.html"
    login_url = "/login/"
    redirect_field_name = "redirect_to"


def form_valid(self, form):
    product = form.save()
    user = self.request.user
    product.owner = user
    user.save()
    return super().form_valid(form)


def get_form_class(self):
    user = self.request.user
    if (user.has_perm("can_delite_product") and user.has_perm("can_change_category") and
            user.has_perm("can_description_product")):
        return ProductModeratorForm
    raise PermissionDenied
