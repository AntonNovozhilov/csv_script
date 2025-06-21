import argparse

REGULAR = r"(.*?)(=|>|<)(.*)"
REGULAR_AGG = r"(.*?)(=)(.*)"


def parse_args():
    """Добавляем аргументы для консоли."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        type=str,
        dest="filename",
        help="Путь до файла, если файл в текущей директории, то его название.",
    )
    parser.add_argument(
        "--where",
        type=str,
        dest="where",
        help='Введите условие для фильтрации данных. Например: "price>100"',
    )
    parser.add_argument(
        "--aggregate",
        type=str,
        dest="aggregate",
        help='Введите условие для агрегации данных. Например: "rating=min"',
    )
    parser.add_argument(
        "--order_by",
        type=str,
        dest="order_by",
        help='Введите условие для агрегации данных. Например: "rating=asc"',
    )
    return parser.parse_args()


args = parse_args()
name = args.filename
where = args.where
order_by = args.order_by
aggregate = args.aggregate
