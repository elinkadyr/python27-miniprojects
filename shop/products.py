from utils import get_products, update_products

def create():
    title = input("Введите название: ")
    price = float(input("Введите цену: "))

    new_product = {'title': title, 'price': price}

    products = get_products()
    products.append(new_product)
    update_products(products)

def read():
    products = get_products()
    for product in products:
        print(f"""
=============================
Название: {product['title']}
Цена: {product['price']}
============================= 
""")

