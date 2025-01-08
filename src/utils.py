import json
import logging
import os.path

from src.config import APP_PATH

logger = logging.getLogger("utils")
log_filepath = os.path.join(APP_PATH, "logs", "utils.log")
file_handler = logging.FileHandler(log_filepath, encoding="utf-8", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operation(json_path: str = '') -> list[dict]:
    """Функция, получающая данные о транзакциях из json-файла
    :param json_path: - путь к json-файлу
    :return: список словарей, представляющих собой транзакции
    """
    logger.info(f"Запуск функции get_operation c параметрами json_path = {json_path}")
    operations = []
    logger.info("Проверка наличия пути к json-файлу в качестве аргумента.")
    if json_path:
        logger.info(
            "Путь к json передан. Формирование полного абсолютного пути к json-файлу"
        )
        json_filepath = os.path.join(APP_PATH, os.path.normpath(json_path))
        logger.info("Проверка валидности пути к json-файлу")
        if os.path.exists(json_filepath):
            logger.info("Путь к json валидный")
            try:
                logger.info("Попытка открытия и чтения json-файла")
                with open(json_filepath, encoding="utf-8") as f:
                    if f:
                        logger.info("json-файл не пустой. Чтение json")
                        operations = json.load(f)
                    if not isinstance(operations, list):
                        logger.error("Файл содержит не список. Возврат пустого списка")
                        return []
                    operations_list = []
                    for operation in operations:
                        if operation:
                            operations_list.append(operation)
                    logger.info("Возврат списка словарей")
                    return operations_list
            except:
                logger.error("Ошибка чтения файла. Возврат пустого списка транзакций")
                return []
        else:
            logger.error("Путь к файлу невалидный. Возврат пустого списка")
            return []
    else:
        logger.error(
            "Путь к json-файлу в качестве аргумента не передан. Возврат пустого списка транзакций"
        )
        return []
