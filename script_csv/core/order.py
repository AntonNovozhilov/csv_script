import re

from tabulate import tabulate
from .validators import check_order_error


def sort_data(data: list, order_by: str) -> list:
    """Сортируем файл по условию которое пропсиано в -order_by."""

    value = check_order_error(data, order_by)
    index = index = data[0].index(value.group(1))
    n = len(data)
    direction = value.group(3)
    for i in range(n):
        for j in range(1, n - i - 1):
            row1 = data[j][index]
            row2 = data[j + 1][index]
            try:
                row1 = float(row1)
                row2 = float(row2)
            except ValueError:
                pass
            if direction == "asc":
                if row1 > row2:
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif direction == "desc":
                if row1 < row2:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                raise ValueError()
    return list([data[0]] + data[1:])


def file_order_by_print(data: list, order_by: str):
    """Выводим отсортированные данные из файла в виде таблицы."""

    sorted_data = sort_data(data, order_by)
    print(tabulate(sorted_data[1:], headers=data[0], tablefmt="outline"))
