from src.masks import get_masks_account, get_masks_card_number
from src.widget import get_date, masks_account_card


def test_function(number, function, data):
    """Функция для проверки реализованных функций, принимающих один аргумент.
    number - номер теста
    function - имя тестируемой функции
    data - данные, принимаемые тестируемой функцией"""
    try:
        result = function(data)
    except Exception as e:
        result = f"Произошла ошибка: {e.__class__} {e.__str__()}"
    print(f"""тест №{number}. Input: {type(data)} {data}. Output: {result}""")


# Тесты

print("Функция get_masks_card_number:")

# тест №1. Задаем функции get_masks_card_number номер карты в верном формате (тип int, 16 цифр)
test_function(1, get_masks_card_number, 7000792289606361)

# тест №2. Задаем функции get_masks_card_number номер карты в верном формате (тип str, символы-только цифры,
# 16 символов)
test_function(2, get_masks_card_number, "7000792289606361")

# Задаем функции get_masks_card_number номер карты в неверном формате (тип int, меньше 16 символов)
test_function(3, get_masks_card_number, "70007926361")

# Задаем функции get_masks_card_number номер карты в неверном формате (тип str, в номере есть буквенные символы)
test_function(4, get_masks_card_number, "A000792289606361")

# Задаем функции get_masks_card_number номер карты с неверным типом данных (тип list)
test_function(5, get_masks_card_number, [1, 2, 3])
print()

print("Функция get_masks_account:")
# Задаем функции get_masks_card_account номер счета в верном формате (тип int)
test_function(1, get_masks_account, 73654108430135874305)

# Задаем функции get_masks_card_account номер счета в верном формате (тип str, символы-только цифры)
test_function(2, get_masks_account, "73654108430135874305")

# Задаем функции get_masks_card_account номер счета в неверном формате (тип str, в номере есть буквенные символы)
test_function(3, get_masks_account, "A3654108430135874305")

# Задаем функции get_masks_card_account номер счета с неверным типом данных (тип list)
test_function(4, get_masks_account, [1, 2, 3])
print()

print('Функция get_data:')
test_function(1, get_date, "2024-03-11T02:26:18.671407")
print()

print("Функция get_account_card:")
test_function(1, masks_account_card, 'Maestro 1596837868705199')
test_function(2, masks_account_card, 'Счет 64686473678894779589')
test_function(3, masks_account_card, 'MasterCard 7158300734726758')
test_function(4, masks_account_card, 'Счет 35383033474447895560')
test_function(5, masks_account_card, 'Visa Classic 6831982476737658')
test_function(6, masks_account_card, 'Visa Platinum 8990922113665229')
test_function(7, masks_account_card, 'Visa Gold 5999414228426353')
test_function(8, masks_account_card, 'Счет 73654108430135874305')

#Задаем функции masks_account_card номер карты в неверном формате (менее 16 символов)
test_function(9, masks_account_card, 'Maestro 868705199')

#Задаем функции masks_account_card номер карты в неверном формате (буква в номере)
test_function(10, masks_account_card, 'Maestro A596837868705199')

#Задаем функции masks_account_card номер карты в неверном формате (тип данных не str)
test_function(11, masks_account_card, [1, 2, 3])

#Задаем функции masks_account_card номер счета в неверном формате (буква в номере)
test_function(12, masks_account_card, 'Счет 73A54108430135874305')