from django.urls import path

from .views import ProductsView, ProductDetailView, ProductCreateView

urlpatterns = [
   path('', ProductsView.as_view()),
   path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
   path('create/', ProductCreateView.as_view(), name='product_create'),
]
