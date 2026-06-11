from app.main import outdated_products
import datetime
from unittest import mock


@mock.patch("datetime.date.today")
def test_outdated_products(mock_date_today: int) -> None:
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
    outdated_products(products)
    assert mock_date_today.called
