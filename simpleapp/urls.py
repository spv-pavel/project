from django.urls import path

from .views import ProductsView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
   path('', ProductsView.as_view()),
   path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
   path('create/', ProductCreateView.as_view(), name='product_create'),
   path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
   path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
