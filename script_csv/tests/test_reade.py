from core.read import reader_file
import pytest
from conftest import data

def test_read_f(data):
    result = reader_file("script_csv/tests/test_file.csv")
    assert data == result


@pytest.mark.parametrize(
    "index, value",
    [
        (0, ["name", "brand", "price", "rating"]),
        (-1, ["poco x5 pro", "xiaomi", "299", "4.4"]),
    ],
)
def test_value_read_f(index, value):
    result = reader_file("script_csv/tests/test_file.csv")
    assert result[index] == value
