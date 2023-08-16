from django.urls import path
from apps.products.api.api import get_all_products, add_product, get_product_by_id, update_product
from apps.products.api.views.product_views import ProductListAPIView, ProductDetailAPIView,\
    ProductCreateAPIView, ProductDestroyAPIView, ProductUpdateAPIView


urlpatterns = [
    path('', ProductListAPIView.as_view(), name='get_all_products_api'),
    path('create/product/', ProductCreateAPIView.as_view(), name='add_product_api'),
    path('read/product/<int:pk>/', ProductDetailAPIView.as_view(), name='get_product_api'),
    path('update/product/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product_api'),
    path('delete/product/<int:pk>/', ProductDestroyAPIView.as_view(), name='delete_product_api')
]