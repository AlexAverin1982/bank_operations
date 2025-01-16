import os.path

import requests
from dotenv import load_dotenv

load_dotenv()


def get_currency_rate(cur_code: str) -> dict:
    """возвращает текущий курс указанной валюты, используя api"""
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    result = {}
    r = requests.get(url)
    if r.ok:
        result = r.json().get("Valute", {})
        try:
            r = result.get(cur_code)
            if r:
                result = {"currency_code": cur_code, "rate": r.get("Value", 0.0)}
            else:
                raise ValueError("Данные по этой валюте отсутствуют")
        except:
            raise ValueError("Данные по этой валюте отсутствуют")

    return result


def convert_currencies(convert_from: str, convert_to: str, amount: float) -> float:
    """конвертирует из одной валюты в другую"""

    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={convert_from}&amount={amount}"
    response = requests.get(url, headers=headers)

    if response.ok:
        return float(response.json()["result"])
    else:
        return 0.0
