from apps.products.models import Cart, Product, Stock

import logging
logger = logging.getLogger(__name__)


def my_scheduled_job():

    cart_products = Cart.objects.all()

    for cart_product in cart_products:
        product_id = cart_product.product_id
        product_quantity = cart_product.product_quantity

        product_stock = Stock.objects.get(id=product_id)
        product_current_stock = product_stock.current_stock
        product_initial_stock = product_stock.initial_stock

        # If the quantity of a product in the cart + the current stock of the product is different
        # from the initial stock of the product, we update the current stock by subtracting the initial stock
        # minus the quantity of the product in the cart
        
        if product_quantity + product_current_stock != product_initial_stock:
            product_stock.current_stock = product_initial_stock - product_quantity
            product_stock.save()


