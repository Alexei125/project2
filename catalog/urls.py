from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, MyView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="base"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="products"),
    path('catalog/create', MyView.as_view(), name='product_form')
]
