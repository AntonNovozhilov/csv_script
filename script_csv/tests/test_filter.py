from core.filter import filter_file
import pytest


@pytest.mark.parametrize(
    "arg, value",
    [
        (
            "price>1000",
            [["galaxy s23 ultra", "samsung", "1199", "4.8"]],
        ),
        ("price>10000", []),
    ],
)
def test_filter_price_one(arg, value, data):
    result = filter_file(data, arg)
    assert result == value


@pytest.mark.parametrize(
    "arg, value",
    [
        (
            "brand=xiaomi",
            [
                ["redmi note 12", "xiaomi", "199", "4.6"],
                ["poco x5 pro", "xiaomi", "299", "4.4"],
            ],
        ),
        (
            "price<300",
            [
                ["redmi note 12", "xiaomi", "199", "4.6"],
                ["poco x5 pro", "xiaomi", "299", "4.4"],
            ],
        ),
    ],
)
def test_filter_price_two(arg, value, data):
    result = filter_file(data, arg)
    assert result == value


@pytest.mark.parametrize(
    "arg, error",
    [
        ("bra=xiaomi", ValueError),
        ("price>>100", ValueError),
        ("a", AttributeError),
    ],
)
def test_error(arg, error, data):
    with pytest.raises(error):
        filter_file(data, arg)
