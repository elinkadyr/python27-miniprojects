from utils import get_products, update_products

def create():
    title = input("введите название: ")
    price = float(input("введите цену: "))

    new_product = {'title': title, 'price': price}

    products = get_products()
    products.append(new_product)
    update_products(products)

def read():
    products = get_products()
    for product in products:
        print(f"""
=============================
название: {product['title']}
цена: {product['price']}
============================= 
""")

def delete():
    products = get_products()
    print(f"выберите продукт для удаления: ")
    for ind, prod in enumerate(products):
        print(f"{ind} => {prod['title']}") 
    index = int(input())
    products.pop(index)
    update_products(products)

def update():
    products = get_products()
    print(f"выберите продукт для обновления: ")
    for ind, prod in enumerate(products):
        print(f"{ind} => {prod['title']}") 
    index = int(input())
    prod = products[index]
    print(f"""
=============================
название: {prod['title']}
цена: {prod['price']}
============================= 
""")
    field = input("какое поле хотите обновить?(title,price)\n")
    value = input("введите значение для этого поля: ")
    if field == 'title':
        prod['title'] = value
    elif field == 'price':
        prod['price'] = float(value)
    update_products(products)
