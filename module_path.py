import re
from collections import Counter


def get_data(path: str) -> list[str]:
    """
    Функция принимает параметр path(имя файла в виде строки). Дальше функция открывает данный файл и
    считывает всю информацию из этого файла, и возвращает ее в виде строки.
    :param path: Имя файла
    :return:
        str: возвращает все что было в считываемом файле
    """
    with open(path, 'r', encoding='utf-8') as file:
        text = file.readlines()
        text = [word.rstrip("\n") for word in text]
        return text


def search_ip(text: str):
    # ip = re.match(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    #                      r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', text)
    list_ip = []
    for i in text:
        re_ip = re.search(r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                          r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$',i)
        if re_ip is not None:
            list_ip.append(re_ip.group())

    # list_ip = ['.'.join(ip) for ip in list_ip]
    print(list_ip)
