def filter_by_currency(list_of_transactions: list, transaction_currency: str = 'USD') -> dict:
    '''
    Функция, принимающая на вход список словарей, представляющих транзакции, и поочередно возвращающая транзакции,
    где валюта операции соответствует заданной (например, USD).
    :param list_of_transactions: список словарей, представляющих собой транзакции
    :param transaction_currency: строка, представляющая собой ключ словаря валюты транзакции. По умолчанию - USD
    :return: словарь, представляющий собой транзакцию, с валютой, соответствующей заданной
    '''
    if not (isinstance(list_of_transactions, list) and isinstance(transaction_currency, str)):
        raise TypeError("Неверный тип данных")
    if not list_of_transactions:
        raise ValueError('Пустой список')
    else:
        transactions_iterator = iter(list_of_transactions)
        for transaction in transactions_iterator:
            if not isinstance(transaction, dict):
                raise TypeError("Неверный тип данных. Ожидается 'dict'")
            if 'operationAmount' not in transaction:
                raise KeyError("Неверный формат данных. Ключ 'operationAmount' отсутствует в словаре")
            if not isinstance(transaction.get('operationAmount'), dict):
                raise TypeError("Неверный тип данных. Ожидается 'dict'")
            if 'currency' not in transaction.get('operationAmount'):
                raise KeyError("Неверный формат данных. Ключ 'currency' отсутствует в словаре")
            if not isinstance(transaction.get('operationAmount').get('currency'), dict):
                raise TypeError("Неверный тип данных. Ожидается 'dict'")
            if 'code' not in transaction.get('operationAmount').get('currency'):
                raise KeyError("Неверный формат данных. Ключ 'code' отсутствует в словаре")
            if transaction.get('operationAmount').get('currency').get('code') == transaction_currency:
                yield transaction


def transaction_descriptions(list_of_transactions: list):
    '''
    Функция, принимающая на вход список словарей с транзакциями и возвращает описание каждой операции по очереди.
    :param list_of_transactions: список словарей, представляющих собой транзакции
    :return: описание транзакции
    '''
    if not isinstance(list_of_transactions, list):
        raise TypeError('Неверный тип данных')
    if not list_of_transactions:
        raise ValueError('Пустой список')
    else:
        transactions_iterator = iter(list_of_transactions)
        for transaction in transactions_iterator:
            if not isinstance(transaction, dict):
                raise TypeError("Неверный тип данных. Ожидается 'dict'")
            if 'description' not in transaction:
                raise KeyError("Неверный формат данных. Ключ 'description' отсутствует в словаре")
            if transaction.get('description'):
                yield transaction.get('description')


def card_number_generator(start: int, stop: int) -> str:
    '''
    Функция-генератор, возвращающая номера карт в формате ХХХХ ХХХХ ХХХХ ХХХХ из диапазона чисел
    от start_number до stop_number.
    :param start_number: начальный номер диапазона генерации
    :param stop_number: конечный номер диапазона генерации
    '''
    if not (isinstance(start, int) and isinstance(stop, int)):
        raise TypeError('Неверный тип данных')
    if start < 0 or stop < 0 or start > stop:
        raise ValueError('Неверное значение переменных')
    number = start
    while number <= stop:
        number_len = len(str(number))
        card_number = ''.join(['0' for x in range(16 - number_len)]) + str(number)
        card_number = card_number[:4] + ' ' + card_number[4:8] + ' ' + card_number[8:12] + ' ' + card_number[12:]
        yield card_number
        number += 1
