from rest_framework.routers import DefaultRouter
from .views_api import ProdukViewSet, KategoriViewSet, StatusViewSet

router = DefaultRouter()
router.register('produk', ProdukViewSet)
router.register('kategori', KategoriViewSet)
router.register('status', StatusViewSet)

urlpatterns = router.urls
