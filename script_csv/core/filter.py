from tabulate import tabulate
from .validators import check_filter_error


def filter_file(data: list, where: str):
    """Фильтруем файл по условию которое пропсиано в -where."""

    new_file = []
    value = check_filter_error(data, where)
    operator = value.group(2)
    index = data[0].index(value.group(1))
    if operator == "=":
        for row in data[1:]:
            if row[index] == value.group(3):
                new_file.append(row)
    elif operator == ">":
        for row in data[1:]:
            if float(row[index]) > float(value.group(3)):
                new_file.append(row)
    elif operator == "<":
        for row in data[1:]:
            if float(row[index]) < float(value.group(3)):
                new_file.append(row)
    return new_file


def file_filter_print(data: list, where: str):
    """Выводим отфильтрованные данные из файла в виде таблицы."""

    try:
        new_file = filter_file(data, where)
        print(tabulate(new_file, headers=data[0], tablefmt="outline"))
    except AttributeError:
        raise AttributeError(
            'Неверный формат фильтрации. Пример: --where "price>100"'
        )
