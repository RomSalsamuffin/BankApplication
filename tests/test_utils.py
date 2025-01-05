import os

import pytest

from src.config import APP_PATH
from src.utils import get_operation


def test_get_operation_no_path():
    """Функция, тестирующая работу функции get_operation с отсутствующим путем к файлу"""
    assert get_operation() == []


def test_get_operation_no_file():
    """Функция, тестирующая работу функции get_operation с путем к файлу json, но без файла"""
    assert get_operation("1.json") == []


@pytest.mark.parametrize(
    "test_data, expected", [("1", []), ('[{"id": 1}]', [{"id": 1}])]
)
def test_get_operation(test_data, expected):
    """Функция, тестирующая работу функции get_operation с json-файлом"""
    json_test_filepath = os.path.join(APP_PATH, "tests", "get_operation_test.json")
    with open(json_test_filepath, "w") as file:
        file.write(test_data)
    assert get_operation(json_test_filepath) == expected
    os.remove(json_test_filepath)
