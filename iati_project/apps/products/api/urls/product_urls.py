from django.urls import path
from apps.products.api.api import get_all_products, add_product, get_product_by_id, update_product
from apps.products.api.views.product_views import ProductListAPIView, ProductDetailAPIView


urlpatterns = [
    path('', ProductListAPIView.as_view(), name='get_all_products_api'),
    path('create/product/', add_product, name='add_product_api'),
    path('read/product/<int:product_id>/', ProductDetailAPIView.as_view(), name='get_product_api'),
    path('update/product/<int:product_id>/', update_product, name='update_product_api')
]