from module_path import *


def main():
    # Считываем текст из файла
    text = get_data("log.txt")
    # Cоздаем список кортежей - (ip адрес, кол-во повторений)
    list_word = search_ip(text)
    # Сортируем список кортежей по кол-во повторений, если кол-во одинаковое, то по длине ip адреса
    list_ip = sorted_ip(list_word)
    # Записываем в новый файл ip адреса и их кол-во повторений в тексте
    file = input("Введите имя файла: ")
    write_file_ip(file, list_ip)


if __name__ == '__main__':
    main()

