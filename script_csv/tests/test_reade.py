from core.read import reader_file, file_print
import pytest

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


def test_read_error():
    with pytest.raises(FileNotFoundError):
        reader_file("script_csv/tests/test_file_not_found.csv")

def test_file_print(data):
    file_print(data)
    assert file_print(data) is None
