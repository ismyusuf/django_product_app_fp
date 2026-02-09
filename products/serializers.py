from rest_framework import serializers
from .models import Produk

class ProdukSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produk
        fields = '__all__'
        extra_kwargs = {
            'nama_produk': {'error_messages': {'blank': 'Nama produk tidak boleh kosong.'}},
            'harga': {'error_messages': {'required': 'Harga tidak boleh kosong.', 'null': 'Harga tidak boleh kosong.'}},
            'kategori': {'error_messages': {'required': 'Kategori harus dipilih.', 'null': 'Kategori harus dipilih.'}},
            'status': {'error_messages': {'required': 'Status harus dipilih.', 'null': 'Status harus dipilih.'}},
        }

    def validate_harga(self, value):
        if value <= 0:
            raise serializers.ValidationError("Harga harus angka > 0")
        return value
