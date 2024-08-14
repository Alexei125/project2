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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


def get_form_class(self):
    user = self.request.user
    if user == self.object.owner:
        return ProductForm
    if user.has_perm(["can_delite_product", "can_change_category",
                      "can_description_product"]):
        return ProductModeratorForm
    raise PermissionDenied
