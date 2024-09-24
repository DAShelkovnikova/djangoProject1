
from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import products_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),

]