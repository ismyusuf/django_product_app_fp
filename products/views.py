from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produk
from .forms import ProdukForm


class ProdukListView(ListView):
    """Menampilkan semua produk yang berstatus 'bisa dijual'."""
    model = Produk
    template_name = "products/produk_list.html"

    def get_queryset(self):
        return Produk.objects.filter(status__nama_status="bisa dijual").select_related('kategori', 'status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_active'] = 'bisa_dijual'
        context['total_semua'] = Produk.objects.count()
        context['total_bisa_dijual'] = Produk.objects.filter(status__nama_status="bisa dijual").count()
        return context


class ProdukSemuaListView(ListView):
    """Menampilkan semua produk tanpa filter."""
    model = Produk
    template_name = "products/produk_list.html"

    def get_queryset(self):
        return Produk.objects.all().select_related('kategori', 'status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_active'] = 'semua'
        context['total_semua'] = Produk.objects.count()
        context['total_bisa_dijual'] = Produk.objects.filter(status__nama_status="bisa dijual").count()
        return context


class ProdukCreateView(CreateView):
    """Form untuk menambah produk baru dengan validasi."""
    model = Produk
    form_class = ProdukForm
    template_name = "products/produk_form.html"
    success_url = reverse_lazy('produk_list')


class ProdukUpdateView(UpdateView):
    """Form untuk edit produk dengan validasi."""
    model = Produk
    form_class = ProdukForm
    template_name = "products/produk_form.html"
    success_url = reverse_lazy('produk_list')


class ProdukDeleteView(DeleteView):
    """Konfirmasi hapus produk."""
    model = Produk
    template_name = "products/produk_confirm_delete.html"
    success_url = reverse_lazy('produk_list')


    