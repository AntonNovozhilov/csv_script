from tabulate import tabulate

from .validators import check_aggregate_error, float_check


def aggregate_file(data: list, aggregate: str):
    """Агрегируем файл по условию которое пропиcано в -aggregate."""

    value = check_aggregate_error(data, aggregate)
    column_name = value.group(1)
    values = value.group(3)
    index = data[0].index(value.group(1))
    list_for_table = [column_name]
    string = data[1][index]
    float_check(string)
    except_value = [float(row[index]) for row in data[1:]]
    if values == "min":
        list_for_table.append(min(except_value))
    elif values == "max":
        list_for_table.append(max(except_value))
    elif values == "avg":
        list_for_table.append(sum(except_value) / len(data[1:]))
    return list_for_table


def file_aggregate_print(data: list, aggregate: str):
    """Выводим агрегированные данные в виде таблицы."""

    result = aggregate_file(data, aggregate)
    print(tabulate([[result[1]]], headers=[result[0]], tablefmt="outline"))
