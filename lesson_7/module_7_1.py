class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()
        return result

    def add(self, *products):
        products_in_shop = self.get_products()
        file = open(self.__file_name, 'a')
        products_to_add = ""
        for product in products:
            if products_in_shop.__contains__(product.name):
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                new_product = f"{product.__str__()}\n"
                products_in_shop += new_product
                products_to_add += new_product
        file.write(products_to_add)


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
