from typing import Union


def get_masks_card_number(card_number: Union[str, int]) -> str:
    """
    Функция, маскирующая номер карты, принимаемый в качестве аргумента.
    Формат маскировки - ХХХХ ХХ** **** ХХХХ, где Х - цифра номера карты.
    Видны первые 6 цифр и последние 4 цифры, остальные символы отображаются
    звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.
    Пример работы функции:
    входной аргумент (номер карты) 7000792289606361
    возвращаемый маскированный номер карты: 7000 79** **** 6361
    """
    if type(card_number) not in [str, int]:
        raise TypeError("Неверный тип данных")
    card_number = str(card_number)
    if len(card_number) != 16 or card_number.isdigit() is False:
        raise ValueError("Неверный формат номера карты")
    card_number_mask = card_number.replace(card_number[6:12], "*" * 6)
    card_number_mask = (
        card_number_mask[:4] + " " + card_number_mask[4:8] + " " + card_number_mask[8:12] + " " + card_number_mask[12:]
    )
    return card_number_mask


def get_masks_account(account_number: Union[str, int]) -> str:
    """
    Функция, маскирующая номер счета, принимаемый в качестве аргумента.
    Формат маскировки - **ХХХХ, где Х - цифра номера счета.
    Видны последние 4 цифры счета, а перед ними - две звездочки
    Пример работы функции:
    входной аргумент (номер счета) 73654108430135874305
    возвращаемый маскированный номер счета: **4305
    """
    if type(account_number) not in [str, int]:
        raise TypeError("Неверный тип данных")
    account_number = str(account_number)
    if account_number.isdigit() is False:
        raise ValueError("Неверный формат номера счета")
    return "**" + account_number[-4:]
