from typing import Iterator


def filter_by_currency(list_of_transactions: list[dict], transaction_currency: str = 'USD') -> Iterator[dict]:
    '''
    Функция, принимающая на вход список словарей, представляющих транзакции, и поочередно возвращающая транзакции,
    где валюта операции соответствует заданной (например, USD).
    :param list_of_transactions: список словарей, представляющих собой транзакции
    :param transaction_currency: строка, представляющая собой ключ словаря валюты транзакции. По умолчанию - USD
    :return: итератор, генерирующий словарь, представляющий собой транзакцию, с валютой, соответствующей заданной
    '''
    for transaction in list_of_transactions:
        try:
            code = transaction['operationAmount']['currency']['code']
        except KeyError:
            continue
        if code == transaction_currency:
            yield transaction


def transaction_descriptions(list_of_transactions: list[dict]) -> Iterator[str]:
    '''
    Функция, принимающая на вход список словарей с транзакциями и возвращает описание каждой операции по очереди.
    :param list_of_transactions: список словарей, представляющих собой транзакции
    :return: описание транзакции
    '''
    for transaction in list_of_transactions:
        if 'description' not in transaction:
            continue
        yield transaction['description']


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    '''
    Функция-генератор, возвращающая номера карт в формате ХХХХ ХХХХ ХХХХ ХХХХ из диапазона чисел
    от start_number до stop_number.
    :param start: начальный номер диапазона генерации
    :param stop: конечный номер диапазона генерации
    '''
    min_card_number = 1
    max_card_number = 9999999999999999
    if (start < min_card_number or start > max_card_number or stop < min_card_number or stop > max_card_number
            or start > stop):
        raise ValueError('Неверное значение переменных')
    number = start
    while number <= stop:
        number_str = str(number)
        card_number = number_str.rjust(16, '0')
        card_number = card_number[:4] + ' ' + card_number[4:8] + ' ' + card_number[8:12] + ' ' + card_number[12:]
        yield card_number
        number += 1
