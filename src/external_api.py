import os.path
from dotenv import load_dotenv
import requests

load_dotenv()


def get_currency_rate(cur_code: str) -> dict:
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    result = {}
    r = requests.get(url)
    if r.ok:
        result = r.json().get('Valute', {})
        r_keys = result.keys()
        if cur_code in r_keys:
            r = result.get(cur_code)

            result = {'currency_code': cur_code, 'rate': r.get('Value', 0.0)}
    return result


def convert_currencies(convert_from: str, convert_to: str, amount: float) -> float:
    """ конвертирует из одной валюты в другую """

    api_key = os.getenv('API_KEY')
    headers = {"apikey": api_key}
    convert_url = f'https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={convert_from}&amount={amount}'
    response = requests.get(convert_url, headers=headers)

    if response.ok:
        return float(response.json()['result'])
    else:
        return 0.0

