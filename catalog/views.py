from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'picture', 'price', 'category']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'picture', 'price', 'category']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class ContactView(TemplateView):
    template_name = "catalog/contact.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # Логика сохранения данных
            return redirect('catalog:contact_success')
        return self.render_to_response(self.get_context_data(form=form))

