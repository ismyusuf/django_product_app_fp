from django.urls import path
from .views import *

urlpatterns = [
    path('', ProdukListView.as_view(), name='produk_list'),
    path('add/', ProdukCreateView.as_view(), name='produk_add'),
    path('edit/<int:pk>/', ProdukUpdateView.as_view(), name='produk_edit'),
    path('delete/<int:pk>/', ProdukDeleteView.as_view(), name='produk_delete'),
]
