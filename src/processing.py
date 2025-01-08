import re
from collections import Counter

from src.generators import transaction_descriptions
from src.widget import get_date


def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED' и возвращает новый список словарей, содержащий только те словари,
     у которых ключ state соответствует указанному значению"""
    if not (isinstance(list_of_dicts, list) and isinstance(state, str)):
        raise TypeError("Неверный тип данных")
    new_list_of_dicts = []
    for el in list_of_dicts:
        if not isinstance(el, dict):
            raise TypeError("Неверный тип данных")
        if "state" not in el:
            raise KeyError("Ключ отсутствует в словаре")
        if el["state"].lower() == state.lower():
            new_list_of_dicts.append(el)
    return new_list_of_dicts


def sort_by_date(list_of_dicts: list, date_reverse_sorting: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате."""
    if not (isinstance(list_of_dicts, list) and isinstance(date_reverse_sorting, bool)):
        raise TypeError("Неверный тип данных")
    for el in list_of_dicts:
        if not isinstance(el, dict):
            raise TypeError("Неверный тип данных")
        if "date" not in el:
            raise KeyError("Ключ отсутствует в словаре")
        get_date(el["date"])

    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=date_reverse_sorting)


def get_transactions_description_sorted_list(transactions_list: list[dict], search_string: str) -> list[dict]:
    '''Функция, принимающая на вход список словарей, представляющих собой транзакции, строку поиска,
    по которой осуществляется сортировка исходного списка. Функция возвращает список словарей, представляющий собой
    транзакции, отсортированные по ключевой фразе
    :param transactions_list - исходный несортированный список словарей, представляющий собой список транзакций
    :param search_string - поисковая строка, по которой осуществляется сортировка списка
    :return transactions_sorted_list - отсортированный список словарей, представляющий собой список транзакций'''
    transactions_sorted_list = []
    for transaction in transactions_list:
        if re.search(search_string.lower(), transaction['description'].lower()):
            transactions_sorted_list.append(transaction)
    return transactions_sorted_list


def count_transactions_categories(transactions_list: list[dict], transactions_categories_list: list) -> dict:
    ''' Функция, принимающая список словарей с данными о банковских операциях и список категорий операций.
    Функция возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории
    :param transactions_list - список словарей, представляющий собой список транзакций
    :param transactions_categories_list - список категорий операций, по которым осуществляется
    подсчет количества операций
    :return transactions_categories_dict - словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории'''
    transactions_categories_dict: dict = dict.fromkeys(transactions_categories_list, 0)
    transactions_description_list = list(transaction_descriptions(transactions_list))
    counted_transactions = dict(Counter(transactions_description_list))
    for transaction_category in counted_transactions:
        if transaction_category in transactions_categories_list:
            transactions_categories_dict[transaction_category] = counted_transactions[transaction_category]
    return transactions_categories_dict
