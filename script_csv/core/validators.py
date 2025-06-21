import re
from arguments.args import REGULAR


def check_filter_error(data: list, where: str):
    """Проверяем корректность фильтрации данных."""

    value = re.match(REGULAR, where)
    column_name = value.group(1)
    if column_name not in data[0]:
        raise ValueError(
            f"Поле '{column_name}' не найдено в заголовках данных."
        )
    operator = value.group(2)
    if operator not in ("=", ">", "<"):
        raise AttributeError("Фильтрация возможна только с оператором '=,<,>'")
    return value


def check_aggregate_error(data: list, aggregate: str):
    """Проверяем корректность агрегирования данных."""

    value = re.match(REGULAR, aggregate)
    if not value:
        raise AttributeError(
            "Некорректный синтаксис агрегирования. Пример: 'price=max'"
        )
    column_name = value.group(1)
    if column_name not in data[0]:
        raise ValueError(
            f"Поле '{column_name}' не найдено в заголовках данных."
        )
    operator = value.group(2)
    if operator != "=":
        raise AttributeError(
            "Агрегирование возможно только по полю с оператором '='"
        )
    values = value.group(3)
    if values not in ("min", "max", "avg"):
        raise IndexError(
            "Допустимы значения для агрегирования: min, max, avg."
        )
    return value


def float_check(value: str):
    """Проверяем, что значение является числом."""

    try:
        float(value)
    except ValueError:
        raise ValueError("Действие возможно только для числовых полей.")


def check_order_error(data: list, order_by: str):
    """Проверяем корректность сортировки данных."""

    value = re.match(REGULAR, order_by)
    if not value:
        raise ValueError(
            "Некорректный синтаксис сортировки. Пример: 'price=asc' или 'price=desc'"
        )
    column_name = value.group(1)
    if column_name not in data[0]:
        raise ValueError(
            f"Поле '{column_name}' не найдено в заголовках данных."
        )
    operator = value.group(2)
    if operator != "=":
        raise AttributeError(
            "Сортировка возможна только с оператором '='"
        )
    values = value.group(3)
    if values not in ("asc", "desc"):
        raise IndexError("Допустимы значения для сортировки: asc, desc.")
    return value
