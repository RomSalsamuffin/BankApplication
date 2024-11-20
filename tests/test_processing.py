import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "input_data, state, expected",
    [
        (123, "CANCELED", TypeError),
        ([1, 2, 3], "CANCELED", TypeError),
        ((1, 2, 3), "CANCELED", TypeError),
        ([{}, {}, {}], "CANCELED", KeyError),
        ([{"state": "CANCELED"}], 1, TypeError),
    ],
)
def test_filter_by_state_exceptions(input_data, state, expected):
    """Функция, тестирующая работу функции filter_by_state с неверным типом данных или с отсутствующим ключом state"""
    with pytest.raises(Exception) as e:
        filter_by_state(input_data, state)
    assert e.type == expected


@pytest.fixture
def get_list_of_dicts_w_executed_in_list_default_state() -> tuple:
    """Фикстура, возвращающая список словарей с параметром по умолчанию state = EXECUTED в словарях,
    отсортированный список"""
    unsorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    "Сортировка по умолчанию state = EXECUTED"
    sorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return unsorted_list, sorted_list


def test_filter_by_state_default_state(
    get_list_of_dicts_w_executed_in_list_default_state,
):
    """Функция, тестирующая работу функции filter_by_state с параметром по умолчанию state = EXECUTED,
    присутствующем в элементах спискаэ"""
    unsorted_list, expected = get_list_of_dicts_w_executed_in_list_default_state
    assert filter_by_state(unsorted_list) == expected


@pytest.fixture
def get_list_of_dicts_w_state_param() -> tuple:
    """Фикстура, возвращающая список словарей, параметр сортировки state = CANCELLED, отсортированный список"""
    unsorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    state = "CANCELED"
    sorted_list = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return unsorted_list, state, sorted_list


def test_filter_by_state_w_state_param_cancelled(get_list_of_dicts_w_state_param):
    """Функция, тестирующая работу функции filter_by_state с параметром state = CANCELED"""
    unsorted_list, state, expected = get_list_of_dicts_w_state_param
    assert filter_by_state(unsorted_list, state) == expected


@pytest.fixture
def get_list_of_dicts_w_state_param_not_in_list() -> tuple:
    """Фикстура, возвращающая список словарей без словарей с указанным state,
    параметр сортировки state, отсортированный список"""
    unsorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    state = "PROCISSING"
    sorted_list = []
    return unsorted_list, state, sorted_list


def test_filter_by_state_wo_state_executed_in_list(
    get_list_of_dicts_w_state_param_not_in_list,
):
    """Функция, тестирующая работу функции filter_by_state с параметром state = PROCESSING"""
    unsorted_list, state, expected = get_list_of_dicts_w_state_param_not_in_list
    assert filter_by_state(unsorted_list, state) == expected


@pytest.mark.parametrize(
    "input_data, date_reverse_sorting, expected",
    [
        (123, False, TypeError),
        ([1, 2, 3], False, TypeError),
        ((1, 2, 3), False, TypeError),
        ([{}, {}, {}], False, KeyError),
        ([{"date": "2019-07-03T18:35:29.512364"}], 1, TypeError),
    ],
)
def test_sort_by_date_exceptions(input_data, date_reverse_sorting, expected):
    """Функция, тестирующая работу функции filter_by_state с неверным типом данных или с отсутствующим ключом state"""
    with pytest.raises(Exception) as e:
        sort_by_date(input_data, date_reverse_sorting)
    assert e.type == expected


@pytest.fixture
def get_list_of_dicts_sorted_by_date_default() -> tuple:
    """Фикстура, возвращающая список словарей, отсортированный список по умолчанию (по убыванию даты)"""
    unsorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    "date_reverse_sorting = True (по убыванию даты)"
    sorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return unsorted_list, sorted_list


def test_sort_by_date_default_sorting(get_list_of_dicts_sorted_by_date_default):
    """Функция, тестирующая работу функции sort_by_date с параметром по умолчанию True (по убыванию даты)"""
    unsorted_list, expected = get_list_of_dicts_sorted_by_date_default
    assert sort_by_date(unsorted_list) == expected


@pytest.fixture
def get_list_of_dicts_sorted_by_date_rising() -> tuple:
    """Фикстура, возвращающая список словарей, параметр сортировки по возрастанию даты, отсортированный список"""
    unsorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    date_reverse_sorting = False
    sorted_list = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return unsorted_list, date_reverse_sorting, sorted_list


def test_sort_by_date_rising_sorting(get_list_of_dicts_sorted_by_date_rising):
    """Функция, тестирующая работу функции sort_by_date с сортировкой по возрастанию даты"""
    unsorted_list, date_reverse_sorting, expected = (
        get_list_of_dicts_sorted_by_date_rising
    )
    assert sort_by_date(unsorted_list, date_reverse_sorting) == expected


@pytest.fixture
def get_list_of_dicts_sorted_by_date_rising_equal_date() -> tuple:
    """Фикстура, возвращающая список словарей с одинаковыми датами, параметр сортировки по возрастанию даты,
    отсортированный список"""
    unsorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
    ]
    date_reverse_sorting = False
    sorted_list = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return unsorted_list, date_reverse_sorting, sorted_list


def test_sort_by_date_rising_sorting_equal_date(
    get_list_of_dicts_sorted_by_date_rising_equal_date,
):
    """Функция, тестирующая работу функции sort_by_date с сортировкой по возрастанию даты"""
    unsorted_list, date_reverse_sorting, expected = (
        get_list_of_dicts_sorted_by_date_rising_equal_date
    )
    assert sort_by_date(unsorted_list, date_reverse_sorting) == expected


@pytest.fixture
def get_list_of_dicts_incorrect_date() -> list:
    """Фикстура, возвращающая список словарей с некорректной датой"""
    unsorted_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018_06-30"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
    ]
    return unsorted_list


def test_sort_by_date_incorrect_date(get_list_of_dicts_incorrect_date):
    """Функция, тестирующая работу функции sort_by_date с некорректной датой"""
    with pytest.raises(ValueError) as e:
        sort_by_date(get_list_of_dicts_incorrect_date)
    assert e.type == ValueError
