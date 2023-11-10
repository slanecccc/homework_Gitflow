import re
from collections import Counter


def get_data(path: str) -> str:
    """
    Функция принимает параметр path(имя файла в виде строки). Дальше функция открывает данный файл и
    считывает всю информацию из этого файла, и возвращает ее в виде строки.
    :param path: Имя файла
    :return:
        str: возвращает все что было в считываемом файле
    """
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        return text


def correctness_ip(ip: str):
    """
    Функция принимает параметр ip (строку) и с помощью регулярного выражения
    проверяет, является ли данный параметр ip4.
    :param ip: Строка
    :return:
        возвращает объект match, если парамерт ip соответсвует шаблону
        None: если параметр ip не соответсвует шаблогу
    """
    cor_ip = re.match(r"((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip)
    return cor_ip


def search_ip(text: str) -> list[tuple]:
    """
    Функция принимает параметр text(строка), дальше функция разбивает текс на отдельные слова и создает список,
    после функция берет каждый элемент созданного списка и проверяет с помощью функции correctness_ip относится
    ли элемент к ip4 адресу и создает с ними отдельный список. После функция создает множество со всеми ip адресами,
    и после этого создает список кортежей, где в кортеже записан ip адрес и его кол-во повторений в тексте, и
    возвращает данный список кортежей
    :param text: Строковой тип
    :return:
        объект Counter

    """
    while text.count("\n") > 0:
        text = text.replace("\n", " ")
    list_word = text.split(" ")
    list_ip = [ip for ip in list_word if correctness_ip(ip)]
    set_ip = set(list_ip)
    list_ip = [(i, list_ip.count(i)) for i in set_ip]
    return list_ip
