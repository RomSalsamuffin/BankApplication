# Проект "BankApplication"

## Описание
Проект "BankApplication" предназначен для управления 
данными банковских аккаунтов и счетов.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/RomSalsamuffin/BankApplication.git
```
## Структура
### Пакет src
Содержит модули для обработки данных банковских аккаунтов и счетов
#### Модуль generators:
* Функция filter_by_currency - предназначена для сортировки списка словарей, представляющих собой транзакции
по валюте транзакции (по умолчанию - USD)
```
Входной аргумент list_of_transactions: список словарей, представляющих собой транзакции
transaction_currency: строка, представляющая собой ключ словаря валюты транзакции. По умолчанию - USD
Возвращаемое значение - словарь, представляющий собой транзакцию, с валютой, соответствующей заданной
```

* Функция transaction_descriptions - функция, принимающая на вход список словарей с транзакциями 
и возвращает описание каждой операции по очереди.
```
Входной аргумент list_of_transactions: список словарей, представляющих собой транзакции
Возвращаемое значение - описание транзакции
```

* Функция card_number_generator - функция-генератор, возвращающая номера карт 
в формате ХХХХ ХХХХ ХХХХ ХХХХ из диапазона чисел от start_number до stop_number.
```
Аргументы:
start_number: начальный номер диапазона генерации
stop_number: конечный номер диапазона генерации
Возвращаемое значение - номер карты в заданном диапазоне
```

#### Модуль masks:
* функция get_masks_card_number - предназначена для маскирования номера банковской карты
```
Входной аргумент (номер карты): 7000792289606361
Вызов функции: get_masks_card_number(7000792289606361)
Возвращаемый маскированный номер карты: 7000 79** **** 6361
```
* функция get_masks_account - предназначена для маскирования номера банковского счета
```
Входной аргумент (номер счета): 73654108430135874305
Вызов функции: get_masks_account(73654108430135874305)
Возвращаемый маскированный номер счета: **4305
```
#### Модуль processing:
* функция filter_by_state - предназначена для сортировки списка словарей по ключу state. 
    По умолчанию - ключ state - 'EXECUTED'
```
Входной аргумент (список словарей): 
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Вызов функции c параметром по умолчанию 'EXECUTED': 
filter_by_state(list_of_dicts)

Вызов функции c передачей второго аргумента: 
filter_by_state(list_of_dicts, 'CANCELLED')

Возвращаемый список словарей: 
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

* функция sort_by_date - предназначена для сортировки списка словарей по дате. 
    По умолчанию - по убыванию. 
```
Входной аргумент (список словарей): 
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Вызов функции (с сортировкой по умолчанию - по убыванию даты):
sort_by_date(list_of_dicts)
Вызов функции (с сортировкой по возрастанию даты):
sort_by_date(list_of_dicts, False)

# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции (сортировка по возрастанию, т. е. сначала самые давние операции)
[{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

#### Модуль widget:
* функция masks_account_card - предназначена для маскирования номера счета или карты
```
Входной аргумент: 'Visa Platinum 7000792289606361'
Вызов функции: masks_account_card('Visa Platinum 7000792289606361')
Возвращаемый маскированный номер карты: 'Visa Platinum 7000 79** **** 6361'

Входной аргумент (номер счета): 'Счет 73654108430135874305'
Вызов функции: masks_account_card("Счет 73654108430135874305")
Возвращаемый маскированный номер счета: 'Счет **4305'
```
* функция get_date - функция, возвращающая дату в формате ДД.ММ.ГГГГ
```
Входной аргумент: '2024-03-11T02:26:18.671407'
Вызов функции: get_date('2024-03-11T02:26:18.671407')
Возвращаемое значение: '11.03.2024'
```

### Пакет tests
Содержит модули для тестирования реализованных функций.
#### Модуль test_generators
Содержит функции для тестирования функций модуля generators.py
* test_filter_by_currency_errors - Функция, тестирующая работу функции filter_by_currency с ошибочными параметрами
* get_usd_sorted_transactions - Фикстура, возвращающая список транзакций, отсортированный по валюте USD
* test_filter_by_currency_default - Функция, тестирующая функцию filter_by_currency c фильтрацией списка 
по валюте USD (по умолчанию)
* test_filter_by_currency_usd - Функция, тестирующая функцию filter_by_currency c фильтрацией списка по валюте USD
* get_rub_sorted_transactions - Фикстура, возвращающая список транзакций, отсортированный по валюте RUB
* test_filter_by_currency_rub - Функция, тестирующая функцию filter_by_currency c фильтрацией списка по валюте RUB
* test_filter_by_currency_none - Функция, тестирующая функцию filter_by_currency c фильтрацией списка по валюте, 
отсутствующей в списке
* test_transaction_descriptions_errors - Функция, тестирующая работу функции filter_by_currency с ошибочными параметрами
* test_transaction_descriptions - Функция, тестирующая функцию transaction_descriptions
* test_card_number_generator - Функция, тестирующая работу функции card_number_generator

#### Модуль test_masks
Содержит функции для тестирования функций модуля masks.py
* test_masks_card_number_valid_int - Функция, тестирующая работу функции get_masks_card_number в целочисленном формате
* test_masks_card_number_valid_str - Функция, тестирующая работу функции get_masks_card_number в формате строки
* test_masks_card_number_invalid_data_type - Функция, тестирующая работу функции get_masks_card_number 
c неверным типом данных
* test_masks_card_number_invalid_forma - Функция, тестирующая работу функции get_masks_card_number 
c неверным форматом карты
* test_masks_card_number_empty_input - Функция, тестирующая работу функции get_masks_card_number c пустой строкой
* test_masks_card_number_parametrize - Функция, тестирующая работу функции get_masks_card_number 
c различными входными данными
* test_masks_account_parametrize - Функция, тестирующая работу функции get_masks_account c различными входными данными

#### Модуль test_processing
Содержит функции для тестирования функций модуля processing.py
* test_filter_by_state_exceptions - Функция, тестирующая работу функции filter_by_state с неверным типом данных 
или с отсутствующим ключом state
* test_filter_by_state_default_state - Функция, тестирующая работу функции filter_by_state 
с параметром по умолчанию state = EXECUTED, присутствующем в элементах списка
* test_filter_by_state_w_state_param_cancelled - Функция, тестирующая работу функции filter_by_state 
с параметром state = CANCELED
* test_filter_by_state_wo_state_executed_in_list - Функция, тестирующая работу функции filter_by_state 
с параметром state = PROCESSING
* test_sort_by_date_exceptions - Функция, тестирующая работу функции filter_by_state с неверным типом данных 
или с отсутствующим ключом state
* test_sort_by_date_default_sorting - Функция, тестирующая работу функции sort_by_date 
с параметром по умолчанию True (по убыванию даты)
* test_sort_by_date_rising_sorting - Функция, тестирующая работу функции sort_by_date с сортировкой по возрастанию даты
* test_sort_by_date_rising_sorting_equal_date - Функция, тестирующая работу функции sort_by_date 
с сортировкой по возрастанию даты
* test_sort_by_date_incorrect_date - Функция, тестирующая работу функции sort_by_date с некорректной датой

#### Модуль test_widget
Содержит функции для тестирования функций модуля widget.py
* test_masks_account_card_parametrize - Функция, тестирующая работу функции get_masks_account 
c различными входными данными
* test_get_date - Функция, тестирующая работу функции get_date c различными входными данными

### Файл main.py
Файл, содержащий реализующий основную логику приложения.

## Использование:

1. Установите проект в локальный репозиторий.
2. Используйте реализованные функции для управления данными о банковском аккаунте - маскирование номера счета, карты, 
номера аккаунта, сортировка операций по дате, статусу.

## Документация:

Для получения дополнительной информации обратитесь к README.md.

## Лицензия:

Этот проект лицензирован по лицензии MIT.



