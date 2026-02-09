from django.db import models

# products/models.py
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori


class Status(models.Model):
    nama_status = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_status


class Produk(models.Model):
    nama_produk = models.CharField(max_length=200)
    harga = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk