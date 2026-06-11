from app.main import outdated_products
import datetime
from unittest import mock


@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_date_today: int) -> None:
    mock_date_today.return_value = datetime.date(2026, 6, 11)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 10, 2),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 10, 22),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2026, 6, 9),
            "price": 160
        }
    ]
    result = outdated_products(products)
    assert result == ["salmon"]
