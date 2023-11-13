from forex_python.converter import CurrencyRates

def get_exchange_rate(base_currency, target_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(base_currency, target_currency)
    return exchange_rate

def convert_currency(base_currency, target_currency, amount):
    exchange rate get_exchange_rate(base_currency, target_currency)