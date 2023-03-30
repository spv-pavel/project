from datetime import datetime
# from pprint import pprint
# from django.views import View  # импортируем простую вьюшку
# from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView, UpdateView
# from django.core.paginator import Paginator

from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm


class ProductsView(ListView):
    model = Product
    template_name = 'simpleapp/products.html'
    context_object_name = 'products'
    ordering = '-price'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ProductDetailView(DetailView):
    template_name = 'simpleapp/product_detail.html'
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm
