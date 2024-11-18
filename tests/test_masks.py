import pytest


from src.masks import get_masks_account, get_masks_card_number


def test_masks_card_number_valid_int():
    """
    Функция, тестирующая работу функции get_masks_card_number в целочисленном формате
    """
    assert get_masks_card_number(7000792289606361) == '7000 79** **** 6361'


@pytest.fixture
def get_card_number_valid_str() -> str:
    '''
    Фикстура, возвращающая номер карты в строковом типе данных
    '''
    return '7000792289606361'


def test_masks_card_number_valid_str(get_card_number_valid_str: str):
    """
    Функция, тестирующая работу функции get_masks_card_number в формате строки
    """
    assert get_masks_card_number(get_card_number_valid_str) == '7000 79** **** 6361'


@pytest.fixture
def get_card_number_list_type() -> list:
    '''
    Фикстура, возвращающая номер карты в формате списка
    '''
    return [1, 2, 3]


def test_masks_card_number_invalid_data_type(get_card_number_list_type: list):
    """
    Функция, тестирующая работу функции get_masks_card_number c неверным типом данных
    """
    with pytest.raises(TypeError) as e:
        get_masks_card_number(get_card_number_list_type)
    assert str(e.value) == "Неверный тип данных"


def test_masks_card_number_invalid_format():
    """
    Функция, тестирующая работу функции get_masks_card_number c неверным форматом карты
    """
    with pytest.raises(ValueError) as e:
        get_masks_card_number("70007926361")
    assert str(e.value) == "Неверный формат номера карты"


def test_masks_card_number_empty_input():
    """
    Функция, тестирующая работу функции get_masks_card_number c пустой строкой
    """
    with pytest.raises(ValueError) as e:
        get_masks_card_number('')
    assert str(e.value) == "Неверный формат номера карты"


@pytest.mark.parametrize('card_number, expected',
                         [
                             (7000792289606361, '7000 79** **** 6361'),
                             ('7000792289606361', '7000 79** **** 6361'),
                             ([1, 2, 3], TypeError),
                             ((1, 2, 3), TypeError),
                             (70007926361, ValueError),
                             ('70007926361', ValueError),
                             ('', ValueError)

                         ]
                         )
def test_masks_card_number_parametrize(card_number, expected):
    """
    Функция, тестирующая работу функции get_masks_card_number c различными входными данными
    """
    try:
        assert get_masks_card_number(card_number) == expected
    except:
        with pytest.raises(Exception) as e:
            get_masks_card_number(card_number)
        assert e.type == expected


@pytest.mark.parametrize('account_number, expected',
                         [
                             (73654108430135874305, '**4305'),
                             ('73654108430135874305', '**4305'),
                             ([1, 2, 3], TypeError),
                             ('', ValueError),
                             ('A3654108430135874305', ValueError)

                         ]
                         )
def test_masks_account_parametrize(account_number, expected):
    """
    Функция, тестирующая работу функции get_masks_account c различными входными данными
    """
    try:
        assert get_masks_account(account_number) == expected
    except:
        with pytest.raises(Exception) as e:
            get_masks_account(account_number)
        assert e.type == expected
