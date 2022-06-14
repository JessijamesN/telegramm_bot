import requests
import json
from config import keys

class ConvertionException(Exception):
    pass


class CryptoConverter():
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f"Одинаковые валюты {base}.")

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Неудалось обработать {quote}")

        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConvertionException(f"Неудалось обработать {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Неудалось обработать количество {amount}")

        f = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}")
        total_base = json.loads(f.content)[keys[base]]

        return total_base
