import csv

from core.read import reader_file, file_print
import pytest


def test_read_f(data):
    result = reader_file("tests/test_file.csv")
    assert data == result


@pytest.mark.parametrize(
    "index, value",
    [
        (0, ["name", "brand", "price", "rating"]),
        (-1, ["poco x5 pro", "xiaomi", "299", "4.4"]),
    ],
)
def test_value_read_f(index, value):
    result = reader_file("tests/test_file.csv")
    assert result[index] == value
