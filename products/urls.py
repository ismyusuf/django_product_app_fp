from django.urls import path
from .views import (
    ProdukListView, ProdukSemuaListView,
    ProdukCreateView, ProdukUpdateView, ProdukDeleteView
)

urlpatterns = [
    path('', ProdukListView.as_view(), name='produk_list'),                # Filter: bisa dijual
    path('semua/', ProdukSemuaListView.as_view(), name='produk_semua'),     # Semua produk
    path('add/', ProdukCreateView.as_view(), name='produk_add'),
    path('edit/<int:pk>/', ProdukUpdateView.as_view(), name='produk_edit'),
    path('delete/<int:pk>/', ProdukDeleteView.as_view(), name='produk_delete'),
]
