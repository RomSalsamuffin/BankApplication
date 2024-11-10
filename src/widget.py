from typing import Union
from src.masks import get_masks_card_number, get_masks_account


def masks_account_card(account_number_str: str) -> str:
    """
    Функция, принимающая номер карты или счета и маскирующая его.

    Формат маскировки номера карты - Имя карты ХХХХ ХХ** **** ХХХХ, где Х - цифра номера карты.
    Видны первые 6 цифр и последние 4 цифры, остальные символы отображаются
    звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.
    Пример работы функции:
    входной аргумент: Visa Platinum 7000792289606361
    возвращаемый маскированный номер карты: Visa Platinum 7000 79** **** 6361

    Формат маскировки номера счета  - Счет **ХХХХ, где Х - цифра номера счета.
    Видны последние 4 цифры счета, а перед ними - две звездочки
    Пример работы функции:
    входной аргумент (номер счета): Счет 73654108430135874305
    возвращаемый маскированный номер счета: Счет **4305
    """
    if type(account_number_str) not in [str]:
        raise TypeError("Неверный тип данных")
    account_number_list = account_number_str.split()
    if len(account_number_list[-1]) == 16 and account_number_list[0] != 'Счет':
        account_number_list[-1] = get_masks_card_number(account_number_list[-1])
    elif account_number_list[0] == 'Счет':
        account_number_list[-1] = get_masks_account(account_number_list[-1])
    else:
        raise ValueError("Неверный формат данных")
    mask_account_number = ' '.join(account_number_list)
    return mask_account_number


def get_date(date_input_str: str) -> str:
    """
    Функция, возвращающая дату в формате ДД.ММ.ГГГГ
    :param date_input_str: Дата в формате '2024-03-11T02:26:18.671407'
    :return: date_str: Дата в формате ДД.ММ.ГГГГ
    """
    if type(date_input_str) not in [str]:
        raise TypeError("Неверный тип данных")
    if "T" not in date_input_str:
        raise ValueError("Неверный формат данных")
    else:
        date_str = '.'.join(date_input_str.split('T')[0].split("-")[-1::-1])
    return date_str