from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product
from items.forms import ProductForm, VersionForm
from items.models import Item, Version


class ItemListView(ListView):
    model = Item

    def get_item(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ItemDetailView(DetailView):
    model = Item

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ItemCreateView(CreateView):
    model = Item
    form_class = ProductForm
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ProductForm
    success_url = reverse_lazy('blog:blogpost_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            form.instance = self.object
            form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('blog:blogpost_detail', args=[self.kwargs.get('pk')])


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('blog:blogpost_list')
