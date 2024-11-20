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
        if el["state"] == state:
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
