from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produk
from .forms import ProdukForm

class ProdukListView(ListView):
    model = Produk
    template_name = "products/produk_list.html"
    def get_queryset(self):
        return Produk.objects.filter(status__nama_status="bisa dijual")


class ProdukCreateView(CreateView):
    model = Produk
    form_class = ProdukForm
    template_name = "products/produk_form.html"
    success_url = reverse_lazy('produk_list')


class ProdukUpdateView(UpdateView):
    model = Produk
    form_class = ProdukForm
    template_name = "products/produk_form.html"
    success_url = reverse_lazy('produk_list')


class ProdukDeleteView(DeleteView):
    model = Produk
    template_name = "products/produk_confirm_delete.html"
    success_url = reverse_lazy('produk_list')


    