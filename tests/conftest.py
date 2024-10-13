import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ])


@pytest.fixture
def category_2():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ])


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


@pytest.fixture
def product_2():
    return Product("55\" QLED 4K",
                   "Фоновая подсветка",
                   123000.0, 7)
