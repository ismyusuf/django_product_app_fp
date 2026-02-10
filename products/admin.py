from django.contrib import admin
from .models import Produk, Kategori, Status


@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_kategori')
    search_fields = ('nama_kategori',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_status')
    search_fields = ('nama_status',)


@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_produk', 'harga', 'kategori', 'status')
    list_filter = ('kategori', 'status')
    search_fields = ('nama_produk',)
