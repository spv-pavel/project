from datetime import datetime
# from pprint import pprint
# from django.views import View  # импортируем простую вьюшку
# from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.core.paginator import Paginator

from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm


class ProductsView(ListView):
    model = Product
    template_name = 'simpleapp/products.html'
    context_object_name = 'products'
    ordering = '-price'
    paginate_by = 4
    # form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        # context['form'] = ProductForm()
        # context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'simpleapp/product_detail.html'
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте,
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


class ProductDeleteView(DeleteView):
    template_name = 'simpleapp/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'
