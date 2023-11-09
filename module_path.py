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


def search_ip(text: str):
    while text.count("\n") > 0:
        text = text.replace("\n", " ")
    list_word = text.split(" ")
    list_ip = []
    for ip in list_word:
        if re.match(r"((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip):
            list_ip.append(ip)
    tuple_ip = Counter(list_ip)
    return tuple_ip
