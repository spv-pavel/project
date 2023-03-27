from django.views.generic import ListView, DetailView

from .models import Product


class ProductsList(ListView):
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # queryset = Product.objects.filter(price__lt=300).order_by('-name')
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'
