from app.main import outdated_products
import datetime
from unittest import mock


@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_date) -> None:
    real_date = datetime.date
    mock_date.today.return_value = real_date(2026, 6, 11)
    mock_date.side_effect = lambda *args, **kwargs: real_date(*args, **kwargs)

    products = [
        {
            "name": "salmon",
            "expiration_date": real_date(2025, 10, 2),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": real_date(2022, 10, 22),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": real_date(2026, 6, 9),
            "price": 160
        }
    ]

    result = outdated_products(products)
    assert result == ["salmon", "chicken", "duck"]