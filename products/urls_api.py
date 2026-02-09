from rest_framework.routers import DefaultRouter
from .views_api import ProdukViewSet

router = DefaultRouter()
router.register('produk', ProdukViewSet)

urlpatterns = router.urls
