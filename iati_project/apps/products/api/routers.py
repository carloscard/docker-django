from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_view import ProductViewSets
from apps.products.api.views.cart_view import CartViewSets
from apps.products.api.views.deliver_view import DeliverViewSets


router = DefaultRouter()
router.register(r'product', ProductViewSets, basename='products')
router.register(r'cart', CartViewSets, basename='carts')
router.register(r'deliver', DeliverViewSets, basename='deliver')

urlpatterns = router.urls