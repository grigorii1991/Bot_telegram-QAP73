import requests
import json
from config import keys

class ApiException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ApiException(f'Невозможно перевести идентичные валюты {base}.')

        try:
            qoute_ticker = keys[quote]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount}')

        request_string = f'https://min-api.cryptocompare.com/data/price?fsym={qoute_ticker}&tsyms={base_ticker}'
        r = requests.get(request_string)
        total_base = json.loads(r.content)[keys[base]] * amount
        return total_base