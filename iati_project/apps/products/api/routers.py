from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSets

router = DefaultRouter()
router.register(r'product', ProductViewSets, basename='products')

urlpatterns = router.urls