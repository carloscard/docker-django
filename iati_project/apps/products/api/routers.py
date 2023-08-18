from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSets
from apps.products.api.views.cart_views import CartViewSets


router = DefaultRouter()
router.register(r'product', ProductViewSets, basename='products')
router.register(r'cart', CartViewSets, basename='carts')

urlpatterns = router.urls