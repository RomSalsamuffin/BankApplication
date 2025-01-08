from src.csv_excel import get_transactions_csv, get_transactions_excel
from src.generators import filter_by_currency
from src.processing import (filter_by_state,
                            get_transactions_description_sorted_list,
                            sort_by_date)
from src.utils import get_operation
from src.widget import get_date, masks_account_card


def main():
    ''' Функция, отвечающая за основную логику взаимодействия проекта с пользователем
    и связывающая функциональности между собой. '''
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')

    while True:
        menu_point = int(input('''Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        >>> '''))
        if menu_point in [1, 2, 3]:
            break
        else:
            print('Данные введены некорректно')
    transactions_list = []
    if menu_point == 1:
        print('Для обработки выбран JSON-файл')
        transactions_list = get_operation('data/operations.json')
    elif menu_point == 2:
        print('Для обработки выбран CSV-файл')
        transactions_list = get_transactions_csv('data/transactions.csv')
    elif menu_point == 3:
        print('Для обработки выбран EXCEL-файл')
        transactions_list = get_transactions_excel('data/transactions_excel.xlsx')
    while True:
        filtering_status = input('''Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        >>> ''').lower()
        if filtering_status not in ['executed', 'canceled', 'pending']:
            print(f'Статус операции {filtering_status} недоступен')
        else:
            break
    if filtering_status == 'executed':
        print('Операции отфильтрованы по статусу "EXECUTED"')
    elif filtering_status == 'canceled':
        print('Операции отфильтрованы по статусу "CANCELED"')
    elif filtering_status == 'pending':
        print('Операции отфильтрованы по статусу "PENDING"')
    transactions_list = filter_by_state(transactions_list, filtering_status)
    while True:
        date_sorting_flag = input("Отсортировать операции по дате? Да/Нет >>> ").lower()
        if date_sorting_flag not in ['да', 'нет']:
            print('Данные введены некорректно')
        else:
            break
    if date_sorting_flag == 'да':
        while True:
            date_rising_sorting_flag = input('Отсортировать по возрастанию или по убыванию? >>> ').lower()
            if date_rising_sorting_flag not in ['по возрастанию', 'по убыванию']:
                print('Данные введены некорректно')
            else:
                break
        if date_rising_sorting_flag == 'по возрастанию':
            date_rising_sorting_flag = False
        elif date_rising_sorting_flag == 'по убыванию':
            date_rising_sorting_flag = True
        transactions_list = sort_by_date(transactions_list, date_rising_sorting_flag)
    while True:
        rub_sorting_flag = input('Выводить только рублевые транзакции? Да/Нет >>> ').lower()
        if rub_sorting_flag not in ['да', 'нет']:
            print('Данные введены некорректно')
        else:
            break
    if rub_sorting_flag == 'да':
        transactions_list = list(filter_by_currency(transactions_list, "RUB"))
    while True:
        keyword_sort_flag = (input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет >>> ').
                             lower())
        if keyword_sort_flag not in ['да', 'нет']:
            print('Данные введены некорректно')
        else:
            break
    if keyword_sort_flag == 'да':
        sorting_keyword = input('Введите слово для поиска >>> ')
        transactions_list = get_transactions_description_sorted_list(transactions_list, sorting_keyword)
    print('Распечатываю итоговый список транзакций...')
    if len(transactions_list) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    print(f'Всего банковских операций в выборке: {len(transactions_list)}\n')
    for transaction in transactions_list:
        transaction_out = (f'{get_date(transaction["date"])} {transaction["description"]}\n'
                           f'{(masks_account_card(transaction['from']) + ' -> ') if transaction.get('from') else ''}'
                           f'{masks_account_card(transaction['to'])}\n'
                           f'Сумма: {transaction['operationAmount']['amount']} '
                           f'{transaction['operationAmount']['currency']['name']}'
                           f'\n')
        print(transaction_out)


main()
