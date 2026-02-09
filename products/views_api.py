from rest_framework.viewsets import ModelViewSet
from .models import Produk
from .serializers import ProdukSerializer

class ProdukViewSet(ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
