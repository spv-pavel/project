from django.forms import ModelForm
from .models import Product


# Создаём модельную форму
class ProductForm(ModelForm):
    # В класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля.
    # Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'quantity']
