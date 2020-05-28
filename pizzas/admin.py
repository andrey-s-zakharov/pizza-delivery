from django.contrib import admin

from pizzas.models import Pizza, Order, Currency


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('address', 'total_price', 'currency', )


admin.site.register(Currency)
