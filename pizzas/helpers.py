from decimal import Decimal

from django.core.cache import cache
from django.conf import settings

from pizzas.models import Currency


def get_currency_rates():
    rates = get_currency_from_cache()
    if rates:
        return rates
    rates = get_currency_from_db()
    if rates:
        return rates
    return fetch_currency_data()


def get_currency_from_cache():
    return cache.get(settings.CURRENCY_DATA_CACHE)


def set_currency_to_cache(rates):
    cache.set(settings.CURRENCY_DATA_CACHE, rates, None)


def get_currency_from_db():
    rates = Currency.currency_rates()
    set_currency_to_cache(rates)
    return rates


def fetch_currency_data():
    """ Get currency rates from settings constatns, in future can be used API (fixer.io) """
    rates = {
        'EUR': settings.EUR_RATE,
        'USD': settings.USD_RATE,
    }
    for name, rate in rates.items():
        Currency.objects.update_or_create(name=name, defaults={'rate': rate})
    return rates


def convert_currency(amount, currency_from, currency_to, currency_rates=None):
    if not currency_rates:
        currency_rates = get_currency_rates()
    if amount is None:
        amount = 0
    return Decimal(amount) * \
        (Decimal(currency_rates.get(currency_to)) / Decimal(currency_rates.get(currency_from)))


def currency_price_dict(currency, unit_price, currency_rates=None):
    if not currency_rates:
        currency_rates = get_currency_rates()
    price_dict = {}
    if not unit_price:
        unit_price = 0
    if currency_rates.get(Currency.EUR):
        price_dict[Currency.EUR] = convert_currency(
            unit_price, currency, Currency.EUR, currency_rates=currency_rates
        )
    if currency_rates.get(Currency.USD):
        price_dict[Currency.USD] = convert_currency(
            unit_price, currency, Currency.USD, currency_rates=currency_rates
        )

    return price_dict
