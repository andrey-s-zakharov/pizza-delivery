from rest_framework import serializers

from pizzas.helpers import currency_price_dict
from pizzas.models import Pizza, Currency, Order, OrderPizzasCount


class PizzaSerializer(serializers.ModelSerializer):
    price_rates = serializers.SerializerMethodField()

    def get_price_rates(self, obj):
        return currency_price_dict(Currency.EUR, obj.price)

    class Meta:
        model = Pizza
        read_only_fields = (
            'id', 'name',
            'image_url', 'price_rates',
        )
        fields = read_only_fields


class OrderPizzasCountSerilazer(serializers.HyperlinkedModelSerializer):

    pizza = serializers.IntegerField(source='pizza.id')

    class Meta:
        model = OrderPizzasCount
        fields = ('pizza', 'pizzas_count', )


class OrderSerializer(serializers.ModelSerializer):

    pizzas_set = OrderPizzasCountSerilazer(many=True)
    currency = serializers.CharField(source='currency.name')

    class Meta:
        model = Order
        fields = (
            'id', 'pizzas_set',
            'address', 'contact_details',
            'total_price', 'delivery_price',
            'currency',
        )

    def create(self, validated_data):
        pizzas_set = validated_data.pop('pizzas_set', [])
        currency = validated_data.pop('currency')
        currency_obj = Currency.objects.filter(name=currency.get('name')).first()
        if currency_obj:
            validated_data['currency'] = currency_obj
        else:
            validated_data['currency'] = Currency.objects.filter(name=Currency.EUR).first()
        order = Order.objects.create(**validated_data)
        for pizza_count_data in pizzas_set:
            pizza_count_data['order'] = order
            pizza_count_data['pizza'] = Pizza.objects.filter(
                pk=pizza_count_data.get('pizza').get('id')).first()
            OrderPizzasCount.objects.create(**pizza_count_data)
        return order
