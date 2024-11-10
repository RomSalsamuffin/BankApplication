def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED' и возвращает новый список словарей, содержащий только те словари,
     у которых ключ state соответствует указанному значению"""

    new_list_of_dicts = []
    for dict in list_of_dicts:
        if dict["state"] == state:
            new_list_of_dicts.append(dict)
    return new_list_of_dicts
