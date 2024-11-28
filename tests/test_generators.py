import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


@pytest.fixture
def get_usd_sorted_transactions() -> list:
    '''Фикстура, возвращающая список транзакций, отсортированный по валюте USD'''
    sorted_list = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }
    ]
    return sorted_list


def test_filter_by_currency_default(get_usd_sorted_transactions):
    '''Функция, тестирующая функцию filter_by_currency c фильтрацией списка по валюте USD (по умолчанию)'''
    assert list(filter_by_currency(transactions)) == get_usd_sorted_transactions


def test_filter_by_currency_usd(get_usd_sorted_transactions):
    '''Функция, тестирующая функцию filter_by_currency c фильтрацией списка по валюте USD'''
    assert list(filter_by_currency(transactions, 'USD')) == get_usd_sorted_transactions


@pytest.fixture
def get_rub_sorted_transactions() -> list:
    '''Фикстура, возвращающая список транзакций, отсортированный по валюте RUB'''
    sorted_list = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    return sorted_list


def test_filter_by_currency_rub(get_rub_sorted_transactions):
    '''Функция, тестирующая функцию filter_by_currency c фильтрацией списка по валюте RUB'''
    assert list(filter_by_currency(transactions, 'RUB')) == get_rub_sorted_transactions


def test_filter_by_currency_none():
    '''Функция, тестирующая функцию filter_by_currency c фильтрацией списка по валюте, отсутствующей в списке'''
    assert list(filter_by_currency(transactions, 'MYR')) == []


def test_filter_by_currency_empty_list():
    '''Функция, тестирующая функцию filter_by_currency c фильтрацией пустого списка'''
    assert list(filter_by_currency([])) == []


def test_transaction_descriptions():
    '''Функция, тестирующая функцию transaction_descriptions'''
    assert list(transaction_descriptions(transactions)) == ['Перевод организации',
                                                            'Перевод со счета на счет',
                                                            'Перевод со счета на счет',
                                                            'Перевод с карты на карту',
                                                            'Перевод организации']


@pytest.mark.parametrize('start, stop, expected',
                         [
                             (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
                             (1, 1, ['0000 0000 0000 0001']),
                             (9999999999999999, 9999999999999999, ['9999 9999 9999 9999'])
                         ])
def test_card_number_generator(start, stop, expected):
    '''
    Функция, тестирующая работу функции card_number_generator (верная генерация в заданном диапазоне)
    :param start: Начальное значение диапазона генерации
    :param stop: Конечное значение диапазона генерации
    :param expected: Ожидаемый результат работы функции
    '''
    assert list(card_number_generator(start, stop)) == expected


@pytest.mark.parametrize('start, stop, expected',
                         [
                             (-1, 5, ValueError),
                             (1, -5, ValueError),
                             (5, 1, ValueError),
                             (1234567890123456789, 123456789012345678900, ValueError)
                         ])
def test_card_number_generator_errors(start, stop, expected):
    '''
    Функция, тестирующая работу функции card_number_generator c неверными значениями переменных
    :param start: Начальное значение диапазона генерации
    :param stop: Конечное значение диапазона генерации
    :param expected: Ожидаемое исключение
    '''
    with pytest.raises(Exception) as e:
        next(card_number_generator(start, stop))
    assert e.type == expected
