import logging
import os.path

import pandas as pd

from src.config import APP_PATH

logger = logging.getLogger("csv_excel")
log_filepath = os.path.join(APP_PATH, "logs", "csv_excel.log")
file_handler = logging.FileHandler(log_filepath, encoding="utf-8", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_csv(csv_path: str = "") -> list[dict]:
    """Функция, получающая данные о транзакциях из csv-файла
    :param csv_path: - путь к csv-файлу
    :return: список словарей, представляющих собой транзакции
    """
    logger.info(
        f"Запуск функции get_transactions_csv c параметрами csv_path = {csv_path}"
    )
    transactions_list = []
    logger.info("Проверка наличия переданного в качестве аргумента пути к csv-файлу")
    if csv_path:
        logger.info(
            "Путь к csv передан. Формирование полного абсолютного пути к csv-файлу"
        )
        csv_filepath = os.path.join(APP_PATH, os.path.normpath(csv_path))
        logger.info("Проверка валидности пути к csv-файлу")
        if os.path.exists(csv_filepath):
            logger.info("Путь к csv валидный")
            try:
                logger.info("Попытка открытия и чтения csv-файла")
                logger.info("Чтение csv в dataframe")
                transactions_df = (
                    pd.read_csv(csv_filepath, delimiter=";")
                    .dropna(how="all")
                    .fillna("")
                    .replace("", None)
                )
                logger.info("формирование списка транзакций из датафрейма")
                for index, row in transactions_df.iterrows():
                    row.id = int(row.id)
                    transactions_list.append(row.to_dict())
                for transaction in transactions_list:
                    transaction['operationAmount'] = {
                        'amount': transaction['amount'],
                        'currency': {
                            'name': transaction['currency_name'],
                            'code': transaction['currency_code']
                        }
                    }
                    transaction.pop('amount', None)
                    transaction.pop('currency_name', None)
                    transaction.pop('currency_code', None)
            except Exception as e:
                print(e)
                logger.error("Ошибка чтения файла. Возврат пустого списка транзакций")
        else:
            logger.error("Путь к файлу невалидный. Возврат пустого списка")
    else:
        logger.error("Путь к csv не передан. Возврат пустого списка транзакций")
    return transactions_list


def get_transactions_excel(excel_path: str = "") -> list[dict]:
    """Функция, получающая данные о транзакциях из excel-файла
    :param excel_path: - путь к excel-файлу
    :return: список словарей, представляющих собой транзакции
    """
    logger.info(
        f"Запуск функции get_transactions_excel c параметрами excel_path = {excel_path}"
    )
    transactions_list = []
    logger.info("Проверка наличия переданного в качестве аргумента пути к excel-файлу")
    if excel_path:
        logger.info(
            "Путь к excel передан. Формирование полного абсолютного пути к excel-файлу"
        )
        excel_filepath = os.path.join(APP_PATH, os.path.normpath(excel_path))
        logger.info("Проверка валидности пути к excel-файлу")
        if os.path.exists(excel_filepath):
            logger.info("Путь к excel валидный")
            try:
                logger.info("Попытка открытия и чтения excel-файла")
                logger.info("Чтение excel в dataframe")
                transactions_df = (
                    pd.read_excel(excel_filepath)
                    .dropna(how="all")
                    .fillna("")
                    .replace("", None)
                )
                logger.info("формирование списка транзакций из датафрейма")
                for index, row in transactions_df.iterrows():
                    row.id = int(row.id)
                    transactions_list.append(row.to_dict())
                for transaction in transactions_list:
                    transaction['operationAmount'] = {
                        'amount': transaction['amount'],
                        'currency': {
                            'name': transaction['currency_name'],
                            'code': transaction['currency_code']
                        }
                    }
                    transaction.pop('amount', None)
                    transaction.pop('currency_name', None)
                    transaction.pop('currency_code', None)
            except:
                logger.error("Ошибка чтения файла. Возврат пустого списка транзакций")
        else:
            logger.error("Путь к файлу невалидный. Возврат пустого списка")
    else:
        logger.error("Путь к excel не передан. Возврат пустого списка транзакций")
    return transactions_list
