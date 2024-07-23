from django.urls import path

from items.apps import ItemsConfig
from items.views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

app_name = ItemsConfig.name

urlpatterns = [
    path('', ItemListView.as_view(), name='blogpost_list'),
    path('blog/<slug:slug>/', ItemDetailView.as_view(), name='blogpost_detail'),
    path('create/', ItemCreateView.as_view(), name='blogpost_form'),
    path('blog/<int:pk>/update/', ItemUpdateView.as_view(), name='blogpost_update'),
    path('blog/<int:pk>/delete/', ItemDeleteView.as_view(), name='blogpost_delete'),
]
