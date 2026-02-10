from rest_framework import serializers
from .models import Produk, Kategori, Status


class KategoriSerializer(serializers.ModelSerializer):
    """Serializer untuk model Kategori."""
    class Meta:
        model = Kategori
        fields = ['id', 'nama_kategori']


class StatusSerializer(serializers.ModelSerializer):
    """Serializer untuk model Status."""
    class Meta:
        model = Status
        fields = ['id', 'nama_status']


class ProdukSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Produk.
    Menampilkan detail kategori dan status secara nested (read),
    dan menerima ID kategori/status saat write.
    """
    kategori_detail = KategoriSerializer(source='kategori', read_only=True)
    status_detail = StatusSerializer(source='status', read_only=True)

    class Meta:
        model = Produk
        fields = [
            'id', 'nama_produk', 'harga',
            'kategori', 'status',
            'kategori_detail', 'status_detail'
        ]
        extra_kwargs = {
            'nama_produk': {'error_messages': {'blank': 'Nama produk tidak boleh kosong.'}},
            'harga': {'error_messages': {'required': 'Harga tidak boleh kosong.', 'null': 'Harga tidak boleh kosong.'}},
            'kategori': {'error_messages': {'required': 'Kategori harus dipilih.', 'null': 'Kategori harus dipilih.'}},
            'status': {'error_messages': {'required': 'Status harus dipilih.', 'null': 'Status harus dipilih.'}},
        }

    def validate_harga(self, value):
        if value <= 0:
            raise serializers.ValidationError("Harga harus angka positif (> 0).")
        return value
