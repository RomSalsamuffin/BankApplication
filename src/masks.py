import logging
import os.path

from src.config import APP_PATH
from typing import Union

logger = logging.getLogger('masks')
log_filepath = os.path.join(APP_PATH, 'logs', 'masks.log')
file_handler = logging.FileHandler(log_filepath, encoding='utf-8', mode='w')
file_formatter =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


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
    logger.info(f'Запуск функции get_masks_card_number с параметрами: card_number = {card_number}')
    if type(card_number) not in [str, int]:
        logger.error('Неверный тип данных номера карты')
        raise TypeError("Неверный тип данных")
    card_number = str(card_number)
    if len(card_number) != 16 or card_number.isdigit() is False:
        logger.error('Неверный формат номера карты (не более 16 символов и только числа')
        raise ValueError("Неверный формат номера карты")
    card_number_mask = card_number.replace(card_number[6:12], "*" * 6)
    card_number_mask = (
        card_number_mask[:4]
        + " "
        + card_number_mask[4:8]
        + " "
        + card_number_mask[8:12]
        + " "
        + card_number_mask[12:]
    )
    logger.info(f'Возвращаем маскированный номер карты клиента card_number_mask = {card_number_mask}')
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
    logger.info(f'Запуск функции get_masks_account с параметрами: account_number = {account_number}')
    masked_account_number = ''
    if type(account_number) not in [str, int]:
        logger.error('Неверный тип данных номера счета')
        raise TypeError("Неверный тип данных")
    account_number = str(account_number)
    if account_number.isdigit() is False:
        logger.error('Неверный формат номера счета')
        raise ValueError("Неверный формат номера счета")
    masked_account_number = "**" + account_number[-4:]
    logger.info(f'Возвращаем маскированный номер счета masked_account_number = {masked_account_number}')
    return masked_account_number

if __name__ == '__main__':
    print(get_masks_card_number('7000792289606361'))
    #print(get_masks_card_number('70007922896'))
    #print(get_masks_card_number('A000792289606361'))

    print(get_masks_account('367968696986554546899845'))