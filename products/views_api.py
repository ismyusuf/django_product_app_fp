from rest_framework.viewsets import ModelViewSet
from .models import Produk, Kategori, Status
from .serializers import ProdukSerializer, KategoriSerializer, StatusSerializer


class KategoriViewSet(ModelViewSet):
    """REST API ViewSet untuk model Kategori."""
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer


class StatusViewSet(ModelViewSet):
    """REST API ViewSet untuk model Status."""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ProdukViewSet(ModelViewSet):
    """REST API ViewSet untuk model Produk (memanfaatkan Serializer)."""
    queryset = Produk.objects.select_related('kategori', 'status').all()
    serializer_class = ProdukSerializer
