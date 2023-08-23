from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.products.api.serializers.deliver_serializer import DeliverSerializer, DeliverCreateSerializer
from apps.products.cruds.crud_deliver import deliver_crud
from apps.products.api.controllers.controller_deliver import ControllerDeliver
import logging

logger = logging.getLogger(__name__)


class DeliverViewSets(viewsets.ModelViewSet):
    serializer_class = DeliverSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return deliver_crud.get_multi()
        return deliver_crud.get(id=pk).first()

    def create(self, request):
        """
        To create a Deliver
        """
        self.serializer_class = DeliverCreateSerializer
        logger.info(f'request data to create a deliver: {request.data}')
        deliver_create_serializer = self.serializer_class(data=request.data)

        if deliver_create_serializer.is_valid():
            controller_deliver = ControllerDeliver(request)
            response, response_status = controller_deliver.send_email_to_customer()

            logger.info(f'Deliver create response code: {response_status}')

            return Response(response, status=response_status)

        return Response(deliver_create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
