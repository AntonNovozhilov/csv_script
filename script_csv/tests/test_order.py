import pytest

from core.order import sort_data, file_order_by_print


@pytest.mark.parametrize(
    "arg, error",
    [
        (
            "name=ascs",
            IndexError,
        ),
        ("name>asc", AttributeError),
        ("namse=ascs", ValueError),
        (" ", ValueError),
    ],
)
def test_error_order_by(arg, error, data):
    with pytest.raises(error):
        sort_data(data, arg)


@pytest.mark.parametrize(
    "arg, value",
    [
        (
            "name=asc",
            [
                ["name", "brand", "price", "rating"],
                ["galaxy s23 ultra", "samsung", "1199", "4.8"],
                ["iphone 15 pro", "apple", "999", "4.9"],
                ["poco x5 pro", "xiaomi", "299", "4.4"],
                ["redmi note 12", "xiaomi", "199", "4.6"],
            ],
        ),
        (
            "name=desc",
            [
                ["name", "brand", "price", "rating"],
                ["redmi note 12", "xiaomi", "199", "4.6"],
                ["poco x5 pro", "xiaomi", "299", "4.4"],
                ["iphone 15 pro", "apple", "999", "4.9"],
                ["galaxy s23 ultra", "samsung", "1199", "4.8"],
            ],
        ),
        (
            "price=desc",
            [
                ["name", "brand", "price", "rating"],
                ["galaxy s23 ultra", "samsung", "1199", "4.8"],
                ["iphone 15 pro", "apple", "999", "4.9"],
                ["poco x5 pro", "xiaomi", "299", "4.4"],
                ["redmi note 12", "xiaomi", "199", "4.6"],
            ],
        ),
        (
            "price=asc",
            [
                ["name", "brand", "price", "rating"],
                ["redmi note 12", "xiaomi", "199", "4.6"],
                ["poco x5 pro", "xiaomi", "299", "4.4"],
                ["iphone 15 pro", "apple", "999", "4.9"],
                ["galaxy s23 ultra", "samsung", "1199", "4.8"],
            ],
        ),
    ],
)
def test_order_by(arg, value, data):
    result = sort_data(data, arg)
    assert result == value
