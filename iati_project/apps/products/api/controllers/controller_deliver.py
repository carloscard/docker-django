from rest_framework import status
from django.utils import timezone

from apps.services.mailjet_service import MailerService
from apps.products.cruds.crud_cart import cart_crud
from apps.products.cruds.crud_products import products


class ControllerDeliver:
    def __init__(self, request):
        self.request = request
        self.total_price = 0
        self.order_date = None
        self.products_description = []

    def send_email_to_customer(self):
        cart_items = cart_crud.get_multi()

        if cart_items:

            for item in cart_items:
                product_in_basket = products.get(id=item.product_id).first()

                self.products_description.append(f'{product_in_basket.product_name}x{item.product_quantity} ')
                self.total_price += product_in_basket.price * item.product_quantity

                item.state = False
                item.save()

            subject = "Detalles de tu compra"
            data = {
                "name": self.request.data.get('name'),
                "surname": self.request.data.get('surname'),
                "total_price": float(self.total_price),
                "order_date": str(timezone.now().date()),
                "products": ''.join(self.products_description),
                "address": self.request.data.get('address'),
                "postal_code": self.request.data.get('postal_code'),
                "phone": self.request.data.get('phone')

            }

            mailer = MailerService(
                "carlos.cardenastest@gmail.com",
                self.request.data.get('email'),
                5036528,
                subject,
                data,
            )
            mailer.with_name_from("Iati prueba Carlos Cardenas")
            # mailer.with_name_to("Nuevo lead contacto")

            mailer.send_email()

            response = {'message': f'The Email has been sent'}
            response_status = status.HTTP_200_OK
            return response, response_status

        response = {'message': f'There are not products in your basket'}
        response_status = status.HTTP_400_BAD_REQUEST
        return response, response_status
