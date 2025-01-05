import os.path


def log(filename: str = ""):
    """Декоратор логирования работы функций, параметров и результата ее выполнения
    :param filename: необязательный параметр, определяющий имя файла лога для записи
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging = f"Function {func.__name__} Ok"
            except Exception as err:
                result = None
                logging = (
                    f"Function {func.__name__} error. Error: {type(err).__name__}. "
                    f"Inputs: {*args, *kwargs.values()}"
                )
            if filename == "":
                print(logging)
            else:
                app_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                if not os.path.splitext(filename)[-1] == ".txt":
                    raise ValueError("Имя файла имеет неверное расширение")
                log_filepath = os.path.join(
                    app_path, "logs", os.path.normpath(filename)
                )
                log_dir_path = os.path.dirname(log_filepath)
                if not os.path.exists(log_dir_path):
                    os.makedirs(log_dir_path)
                with open(log_filepath, "a") as f:
                    f.write(f"{logging} \n")
            return result

        return wrapper

    return decorator
