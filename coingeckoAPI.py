import json
import requests


def getCryptoData (coin, currency, daysback):
    """API call to coingecko for historical coin prices"""
    api_url = ('https://api.coingecko.com/api/v3/coins/' + str(coin) +
        '/market_chart?vs_currency=' + str(currency) +
        '&days=' + str(daysback))

    response = requests.get(api_url).text
    return json.loads(response)
