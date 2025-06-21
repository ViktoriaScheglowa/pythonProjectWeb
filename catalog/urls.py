from django.contrib import admin
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]
