from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import mixins

from pizzas.helpers import get_currency_rates
from pizzas.models import Pizza, Order
from pizzas.serializers import PizzaSerializer, OrderSerializer


class PizzasViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    permission_classes = (AllowAny, )
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class OrdersViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = (AllowAny, )
    serializer_class = OrderSerializer
