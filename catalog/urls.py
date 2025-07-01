from django.contrib import admin
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView, ProductDeleteView, \
    ContactView

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact_success/", ContactView.as_view(), name="contact_success"),
   ]
