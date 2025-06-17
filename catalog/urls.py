from django.contrib import admin
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contact


app_name = CatalogConfig.name
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]
