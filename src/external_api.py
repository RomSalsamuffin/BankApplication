import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_amount_rub(transaction: dict) -> float:
    """Функция, принимающая на вход данные о транзакции и
    возвращающая сумму транзакции в рублях
    :param transaction: словарь, представляющий собой данные о транзакции
    :return amount: сумма транзакции в рублях"""
    transaction_currency = transaction["operationAmount"]["currency"]["code"]
    transaction_amount = transaction["operationAmount"]["amount"]
    if transaction_currency == "RUB":
        return float(transaction_amount)
    else:
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB"
            f"&from={transaction_currency}&amount={transaction_amount}"
        )
        payload: dict = {}
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        result = response.json()
        return float(result["result"])
