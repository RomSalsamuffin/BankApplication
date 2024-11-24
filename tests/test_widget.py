import pytest

from src.widget import get_date, masks_account_card


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ([1, 2, 3], TypeError),
        ("Maestro 868705199", ValueError),
        ("Счет 73A54108430135874305", ValueError),
        ("", ValueError),
    ],
)
def test_masks_account_card_parametrize(account_number, expected):
    """
    Функция, тестирующая работу функции get_masks_account c различными входными данными
    """
    try:
        assert masks_account_card(account_number) == expected
    except:
        with pytest.raises(Exception) as e:
            masks_account_card(account_number)
        assert e.type == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ([1, 2, 3], TypeError),
        ("2024-03-11D02:26:18.671407", ValueError),
        ("2024-03_11T02:26:18.671407", ValueError),
        ("T02:26:18.671407", ValueError),
        ("", ValueError),
    ],
)
def test_get_date(date_str, expected):
    """
    Функция, тестирующая работу функции get_date c различными входными данными
    """
    try:
        assert get_date(date_str) == expected
    except:
        with pytest.raises(Exception) as e:
            get_date(date_str)
        assert e.type == expected
