from django.db import models


class Pizza(models.Model):

    name = models.CharField(max_length=256, verbose_name='Name')
    price = models.DecimalField(help_text='in EUR', decimal_places=2, max_digits=9, verbose_name='Price')
    image = models.ImageField(upload_to='pizzas/', null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return self.image.url


class Currency(models.Model):

    EUR = 'EUR'
    USD = 'USD'

    CURRENCIES = (
        (EUR, 'EUR'),
        (USD, 'USD'),
    )

    name = models.CharField(max_length=5, choices=CURRENCIES, verbose_name='Currency')
    rate = models.DecimalField(help_text='to EUR', max_digits=12, decimal_places=4, verbose_name='Rate')

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    @classmethod
    def currency_rates(cls):
        currency_data = Currency.objects.all().values('rate', 'name')
        currency_dict = {currency.get('name'): currency.get('rate') for currency in currency_data}
        return currency_dict

    def __str__(self):
        return self.name


class Order(models.Model):

    pizzas = models.ManyToManyField(Pizza, through='OrderPizzasCount', verbose_name='Pizzas')
    address = models.CharField(max_length=1024, verbose_name='Address')
    contact_details = models.TextField(null=True, blank=True, verbose_name='Contacts details')
    total_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total price')
    delivery_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Delivery price')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='Currency')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.address}-{self.total_price}'


class OrderPizzasCount(models.Model):

    pizza = models.ForeignKey(Pizza, related_name='orders_set', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='pizzas_set', on_delete=models.CASCADE)
    pizzas_count = models.PositiveIntegerField(default=1, verbose_name='Pizzas count')

    def __str__(self):
        return f'{self.order}-{self.pizza}-{self.pizzas_count}'
