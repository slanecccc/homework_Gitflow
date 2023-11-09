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


def search_ip(text: str):
    while text.count("\n") > 0:
        text = text.replace("\n", " ")
    list_word = text.split(" ")
    list_ip = [ip for ip in list_word if correctness_ip(ip)]
    tuple_ip = Counter(list_ip)
    return tuple_ip
