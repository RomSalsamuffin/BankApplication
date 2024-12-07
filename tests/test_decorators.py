import os

import pytest

from src.decorators import log


@log()
def func1(x: int, y: int, z: int = 2) -> int:
    '''Тестовая функция №1'''
    return x + y + z


def test_console_ok(capsys):
    '''Функция, тестирующая работу декоратора с консолью при успешной работе декорированной функции'''
    func1(1, 3)
    captured = capsys.readouterr()
    assert captured.out == 'Function func1 Ok\n'


@log()
def func2(x: int, y: int, z: int = 2):
    '''Тестовая функция №2'''
    raise ValueError


def test_console_error(capsys):
    '''Функция, тестирующая работу декоратора с консолью при возбуждении ошибок декорированной функции'''
    func2(1, 5, z=3)
    captured = capsys.readouterr()
    assert captured.out == 'Function func2 error. Error: ValueError. Inputs: (1, 5, 3)\n'


@log('test/my_log.txt')
def func3(x: int, y: int, z: int = 2):
    '''Тестовая функция №3'''
    return x + y + z


def test_file_ok():
    '''Функция, тестирующая работу декоратора с выводом лога в файл при успешной работе декорированной функции'''
    func3(1, 3)
    log_filename = 'test/my_log.txt'
    app_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_filepath = os.path.join(app_path, 'logs', os.path.normpath(log_filename))
    log_dir_path = os.path.dirname(log_filepath)
    with open(log_filepath, encoding='utf-8') as f:
        result = f.readline()
    os.remove(log_filepath)
    os.rmdir(log_dir_path)
    assert result == 'Function func3 Ok \n'


@log('test/my_log.txt')
def func4():
    '''Тестовая функция №4'''
    raise ValueError


def test_file_error():
    '''Функция, тестирующая работу декоратора с выводом лога в файл при возбуждении ошибок декорированной функции'''
    func4()
    log_filename = 'test/my_log.txt'
    app_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_filepath = os.path.join(app_path, 'logs', os.path.normpath(log_filename))
    log_dir_path = os.path.dirname(log_filepath)
    with open(log_filepath, encoding='utf-8') as f:
        result = f.readline()
    os.remove(log_filepath)
    os.rmdir(log_dir_path)
    assert result == 'Function func4 error. Error: ValueError. Inputs: () \n'


@log('test/my_log.pdf')
def func5():
    '''Тестовая функция №5.'''
    pass


def test_filename_error():
    '''Функция, тестирующая работу декоратора при возбуждении ошибки декоратора'''
    with pytest.raises(Exception) as e:
        func5()
    assert e.type == ValueError
