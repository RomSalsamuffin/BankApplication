import os
from unittest.mock import Mock, patch

import pandas as pd

from src.config import APP_PATH
from src.csv_excel import get_transactions_csv, get_transactions_excel


def test_get_transactions_csv_no_path():
    """Функция, тестирующая работу функции get_transactions_csv с отсутствующим путем к файлу csv"""
    assert get_transactions_csv() == []


def test_get_transactions_csv_no_file():
    """Функция, тестирующая работу функции get_transactions_csv с переданным путем к файлу csv,
    но с отсутствующим файлом"""
    assert get_transactions_csv("1.csv") == []


@patch("src.csv_excel.pd.read_csv")
def test_get_transaction_csv(mocked_read_csv: Mock):
    """Функция, тестирующая работу функции get_transactions_csv с переданным путем к файлу csv,
    c существующим файлом и мокированием функции read_csv"""
    test_transactions_list = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": 16210,
                "currency": {
                    "currency_name": "Sol",
                    "currency_code": "PEN"
                }
            },
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:30:58Z",
            "operationAmount": {
                "amount": 29740,
                "currency": {
                    "currency_name": "Peso",
                    "currency_code": "COP"
                }
            },
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    test_transactions_df = pd.DataFrame(test_transactions_list)

    mocked_read_csv.return_value = test_transactions_df

    csv_test_filepath = os.path.join(APP_PATH, "tests", "get_transactions_csv_test.csv")
    test_transactions_df.to_csv(
        csv_test_filepath, sep=";", encoding="utf-8", index=False
    )
    assert get_transactions_csv(csv_test_filepath) == test_transactions_list
    os.remove(csv_test_filepath)


def test_get_transactions_excel_no_path():
    """Функция, тестирующая работу функции get_transactions_excel с отсутствующим путем к файлу excel"""
    assert get_transactions_excel() == []


def test_get_transactions_excel_no_file():
    """Функция, тестирующая работу функции get_transactions_excel с переданным путем к файлу excel,
    но с отсутствующим файлом"""
    assert get_transactions_excel("1.xlsx") == []


@patch("src.csv_excel.pd.read_excel")
def test_get_transaction_excel(mocked_read_excel: Mock):
    """Функция, тестирующая работу функции get_transactions_excel с переданным путем к файлу excel,
    c существующим файлом и мокированием функции read_excel"""
    test_transactions_list = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": 16210,
                "currency": {
                    "currency_name": "Sol",
                    "currency_code": "PEN"
                }
            },
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:30:58Z",
            "operationAmount": {
                "amount": 29740,
                "currency": {
                    "currency_name": "Peso",
                    "currency_code": "COP"
                }
            },
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    test_transactions_df = pd.DataFrame(test_transactions_list)

    mocked_read_excel.return_value = test_transactions_df

    excel_test_filepath = os.path.join(
        APP_PATH, "tests", "get_transactions_excel_test.xlsx"
    )
    test_transactions_df.to_excel(excel_test_filepath, index=False)
    assert get_transactions_excel(excel_test_filepath) == test_transactions_list
    os.remove(excel_test_filepath)
