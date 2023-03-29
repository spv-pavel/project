from datetime import datetime
# from pprint import pprint
# from django.views import View  # импортируем простую вьюшку
# from django.shortcuts import render

from django.views.generic import DetailView, ListView
# from django.core.paginator import Paginator

from .models import Product
from .filters import ProductFilter


class ProductsList(ListView):
    model = Product
    ordering = '-price'
    # queryset = Product.objects.filter(price__lt=300).order_by('-name')
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 1  # поставим постраничный вывод в один элемент

    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET,
                                          queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

    # # Метод get_context_data позволяет нам изменить набор данных,
    # # который будет передан в шаблон.
    # def get_context_data(self, **kwargs):
    #     # С помощью super() мы обращаемся к родительским классам
    #     # и вызываем у них метод get_context_data с теми же аргументами,
    #     # что и были переданы нам.
    #     # В ответе мы должны получить словарь.
    #     context = super().get_context_data(**kwargs)
    #     # К словарю добавим текущую дату в ключ 'time_now'.
    #     context['time_now'] = datetime.utcnow()
    #     # Добавим ещё одну пустую переменную,
    #     # чтобы на её примере рассмотреть работу ещё одного фильтра.
    #     context['next_sale'] = "Распродажа в среду!"
    #     # pprint(context)
    #     return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'

# # В отличие от дженериков, которые мы уже знаем, код здесь надо писать самому,
# # переопределяя типы запросов (например гет или пост, вспоминаем рек весты из модуля C5)
# class Products(View):
#     def get(self, request):
#         products = Product.objects.order_by('-price')
#         # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
#         p = Paginator(products, 1)
#         # Берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
#         # Теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами
#         products = p.get_page(request.GET.get('page', 1))
#         data = {
#             'products': products,
#         }
#         return render(request, 'products.html', data)
