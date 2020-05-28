from django.conf.urls import url

from rest_framework import routers
from pizzas.views import PizzasViewSet, OrdersViewSet


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'pizzas', PizzasViewSet, basename='pizzas')
router.register(r'orders', OrdersViewSet, basename='orders')

urlpatterns = router.urls
