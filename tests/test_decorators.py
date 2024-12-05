from src.decorators import log


@log()
def func1(x: int, y: int, z: int = 2) -> int:
    '''Тестовая функция №1'''
    return x + y + z


def test_console_ok(capsys):
    '''Функция, тестирующая работу декоратора с консолью при успешной работе декорированной функции'''
    try:
        func1(1, 3)
        captured = capsys.readouterr()
        assert captured.out == 'Function func1 Ok\n'
    except Exception as e:
        print(f'\nTest error: {type(e).__name__} ({e})')


@log()
def func2(x: int, y: int, z: int = 2):
    '''Тестовая функция №2'''
    raise ValueError


def test_console_error(capsys):
    '''Функция, тестирующая работу декоратора с консолью при возбуждении ошибок декорированной функции'''
    try:
        func2(1, 5, z=3)
        captured = capsys.readouterr()
        assert captured.out == 'Function func2 error. Error: ValueError. Inputs: (1, 5, 3)\n'
    except Exception as e:
        print(f'\nTest error: {type(e).__name__} ({e})')


@log('1/my_log.txt')
def func3(x: int, y: int, z: int = 2):
    '''Тестовая функция №3'''
    return x + y + z


def test_file_ok():
    '''Функция, тестирующая работу декоратора с выводом лога в файл при успешной работе декорированной функции'''
    try:
        func3(1, 3)
    except Exception as e:
        print(f'\nTest error: {type(e).__name__} ({e})')


@log('1/my_log.txt')
def func4(x: int, y: int, z: int = 2):
    '''Тестовая функция №4'''
    raise ValueError


def test_file_error():
    '''Функция, тестирующая работу декоратора с выводом лога в файл при возбуждении ошибок декорированной функции'''
    try:
        func4(1, 5, 3)
    except Exception as e:
        print(f'\nTest error: {type(e).__name__} ({e})')
