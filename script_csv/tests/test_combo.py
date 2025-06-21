import pytest
from core.filter import filter_file
from core.order import sort_data


@pytest.mark.parametrize(
    "arg1, arg2, value",
    [
        (
            "brand=xiaomi",
            "price=asc",
            [   ['name', 'brand', 'price', 'rating'],
                ["redmi note 12", "xiaomi", "199", "4.6"],
                ["poco x5 pro", "xiaomi", "299", "4.4"],
            ],
        ),
    ],
)
def test_combo(arg1, arg2, value, data):
    lis = filter_file(data, arg1)
    lis2 = sort_data([data[0]]+lis, arg2)
    assert lis2 == value
