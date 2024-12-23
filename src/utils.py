import json
import os.path

from src.config import APP_PATH


def get_operation(json_path: str = None) -> list[dict]:
    '''Функция, получающая данные о транзакциях из json-файла
    :param json_path: - путь к json-файлу
    :return: список словарей, представляющих собой транзакции
    '''
    operations = []
    if json_path:
        json_filepath = os.path.join(APP_PATH, os.path.normpath(json_path))
        print(json_filepath)
        if os.path.exists(json_filepath):
            try:
                with open(json_filepath, encoding='utf-8') as f:
                    if f:
                        operations = json.load(f)
                    if not isinstance(operations, list):
                        operations = []
            except:
                operations = []
    return operations
