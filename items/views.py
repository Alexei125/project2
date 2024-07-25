from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from items.models import Item


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
    fields = ('title', 'slug', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ('title', 'slug', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:blogpost_list')

    def get_success_url(self):
        return reverse('blog:blogpost_detail', args=[self.kwargs.get('pk')])


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('blog:blogpost_list')
