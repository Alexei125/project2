from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import base, products

app_name = CatalogConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('catalog/<int:pk>/', products, name='products')
]
