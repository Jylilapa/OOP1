
def test_category_1(category_1):
    assert category_1.name == "Смартфоны"
    assert (category_1.description ==
            "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни")
    assert category_1.products == [
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
    ]


def test_category_count_1(category_1):
    assert category_1.count_category == 2
    assert category_1.count_products == 3


def test_category_2(category_2):
    assert category_2.name == "Телевизоры"
    assert (category_2.description ==
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")
    assert category_2.products == [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]


def test_category_count_2(category_2):
    assert category_2.count_category == 4
    assert category_2.count_products == 1
