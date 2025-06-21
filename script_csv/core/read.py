import csv

from tabulate import tabulate


def reader_file(path: str):
    """Читаем файл."""

    with open(path, "r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        data = list(csv_reader)
        if not data:
            raise FileNotFoundError(
                "Файл не найден. Проверьте имя файла и его наличие в текущей директории."
            )
        return data

def file_print(data: list):
    """Выводим данные из файла в виде таблицы."""

    if data:
        print(tabulate(data[1:], headers=data[0], tablefmt="outline"))
