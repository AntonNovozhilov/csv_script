import pytest
from core.aggregate import aggregate_file


@pytest.mark.parametrize(
    "arg, value",
    [
        ("price=max", ["price", 1199.0]),
        ("price=min", ["price", 199.0]),
        ("rating=avg", ["rating", 4.675]),
    ],
)
def test_aggregate(arg, value, data):
    result = aggregate_file(data, arg)
    assert result == value


@pytest.mark.parametrize(
    "arg, error",
    [
        (
            "name=min",
            ValueError,
        ),
        ("prices=max", ValueError),
        ("price>avg", AttributeError),
        ("price=av", IndexError),
        (" ", AttributeError),
    ],
)
def test_error_aggregate(arg, error, data):
    with pytest.raises(error):
        aggregate_file(data, arg)
