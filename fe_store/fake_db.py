from fe_store.models import (
    ProductType, Attribute, Measure, Product, Association, Value
)

products = [
    {
        "id": "1",
        "name": "Ноутбук Xiaomi Mi Notebook Pro 15.6",
        "type": "Ноутбук",
        "price": "54 000",
        "features": {
            "Процессор": "Core i5",
            "Частота процессора": "1600 МГц",
            "Объем оперативной памяти": "8 Гб",
            "Объем жесткого диска": "256 Гб"
        },
    },
    {
        "id": "2",
        "name": "Ноутбук Xiaomi Mi Notebook Pro 15.6",
        "type": "Ноутбук",
        "price": "58 000",
        "features": {
            "Процессор": "Core i7",
            "Частота процессора": "1800 МГц",
            "Объем оперативной памяти": "16 Гб",
            "Объем жесткого диска": "256 Гб"
        },
    },
    {
        "id": "3",
        "name": "Ноутбук Xiaomi Mi Notebook Air 12.5\"",
        "type": "Ноутбук",
        "price": "37 149",
        "features": {
            "Процессор": "Core M3",
            "Частота процессора": "1200 МГц",
            "Объем оперативной памяти": "8 Гб",
            "Объем жесткого диска": "256 Гб"
        },
    },
    {
        "id": "4",
        "name": "Планшет Apple iPad 32Gb Wi-Fi",
        "type": "Планшет",
        "price": "18 490",
        "features": {
            "Операционная система": "iOS",
            "Процессор": "Apple A9 1800 МГц",
            "Количество ядер": "2",
            "Вычислительное ядро": "ARM8"
        },
    },
]


def create_fake_db(db):
    db.drop_all()
    db.create_all()
    db.session.add(ProductType(name="Ноутбук", mp_name="Ноутбуки"))
    db.session.add(ProductType(name="Планшет", mp_name="Планшеты"))

    db.session.add(Attribute(name="Процессор"))
    db.session.add(Attribute(name="Частота процессора", measure_id=1))
    db.session.add(Attribute(name="Объем оперативной памяти", measure_id=2))
    db.session.add(Attribute(name="Объем жесткого диска", measure_id=2))
    db.session.add(Attribute(name="Операционная система"))
    db.session.add(Attribute(name="Количество ядер"))
    db.session.add(Attribute(name="Вычислительное ядро"))
    db.session.add(Attribute(name="Базовая цена", measure_id=3))

    db.session.add(Measure(name="МГц"))
    db.session.add(Measure(name="Гб"))
    db.session.add(Measure(name="руб"))

    db.session.add(Value(name="Core i5"))
    db.session.add(Value(name="1600"))
    db.session.add(Value(name="8"))
    db.session.add(Value(name="256"))
    db.session.add(Value(name="Core i7"))
    db.session.add(Value(name="1800"))
    db.session.add(Value(name="16"))
    db.session.add(Value(name="Core M3"))
    db.session.add(Value(name="1200"))
    db.session.add(Value(name="iOS"))
    db.session.add(Value(name="Apple A9 1800 МГц"))
    db.session.add(Value(name="2"))
    db.session.add(Value(name="ARM8"))
    db.session.add(Value(name="54000.00"))
    db.session.add(Value(name="58000.00"))
    db.session.add(Value(name="37149.00"))
    db.session.add(Value(name="18490.00"))

    prod_1 = Product(
        name='Ноутбук Xiaomi Mi Notebook Pro 15.6 (Intel Core i5)',
        product_type_id=1,
        image="https://avatars.mds.yandex.net/get-mpic/397397/img_id5839825920611580155.jpeg/5hq"
    )
    prod_2 = Product(
        name='Ноутбук Xiaomi Mi Notebook Pro 15.6 (Intel Core i7)',
        product_type_id=1,
        image="https://avatars.mds.yandex.net/get-mpic/397397/img_id5839825920611580155.jpeg/5hq"
    )
    prod_3 = Product(
        name='Ноутбук Xiaomi Mi Notebook Air 12.5',
        product_type_id=1,
        image="https://avatars.mds.yandex.net/get-mpic/200316/img_id1017256079183483194/6hq"
    )
    prod_4 = Product(
        name='Планшет Apple iPad 32Gb Wi-Fi',
        product_type_id=2,
        image="https://avatars.mds.yandex.net/get-mpic/397397/img_id3899168262031019869/6hq",
    )

    db.session.add_all([prod_1, prod_2, prod_3, prod_4])

    fake_attr = [
        {'product_id': 1, 'attribute_id': 1, 'value_id': 1},
        {'product_id': 1, 'attribute_id': 2, 'value_id': 2},
        {'product_id': 1, 'attribute_id': 3, 'value_id': 3},
        {'product_id': 1, 'attribute_id': 4, 'value_id': 4},
        {'product_id': 1, 'attribute_id': 8, 'value_id': 14},

        {'product_id': 2, 'attribute_id': 1, 'value_id': 5},
        {'product_id': 2, 'attribute_id': 2, 'value_id': 6},
        {'product_id': 2, 'attribute_id': 3, 'value_id': 7},
        {'product_id': 2, 'attribute_id': 4, 'value_id': 4},
        {'product_id': 2, 'attribute_id': 8, 'value_id': 15},

        {'product_id': 3, 'attribute_id': 1, 'value_id': 8},
        {'product_id': 3, 'attribute_id': 2, 'value_id': 9},
        {'product_id': 3, 'attribute_id': 3, 'value_id': 3},
        {'product_id': 3, 'attribute_id': 4, 'value_id': 4},
        {'product_id': 3, 'attribute_id': 8, 'value_id': 16},

        {'product_id': 4, 'attribute_id': 5, 'value_id': 10},
        {'product_id': 4, 'attribute_id': 1, 'value_id': 11},
        {'product_id': 4, 'attribute_id': 6, 'value_id': 12},
        {'product_id': 4, 'attribute_id': 7, 'value_id': 13},
        {'product_id': 4, 'attribute_id': 8, 'value_id': 17},

    ]

    for attr in fake_attr:
        db.session.add(Association(
            product_id=attr['product_id'],
            attribute_id=attr['attribute_id'],
            value_id=attr['value_id']
            )
        )

    db.session.commit()
