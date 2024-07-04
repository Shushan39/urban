class Product:
    """
    Объекты класса будут обладать свойствами:
     name - название продукта (строка)
     weight - общий вес товара (дробное число)
     category - категория товара (строка)
    """

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


# Метод __str__ возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        products = ''
        file = open(self.__file_name, 'r', encoding='utf-8')
        products = file.read().strip()
        file.close()
        return products

    def add(self, *products):
        product_names = set()

        # Открываем файл для чтения, чтобы проверить существующие продукты
        file_read = open(self.__file_name, 'r', encoding='utf-8')
        for line in file_read:
            name = line.strip().split(',')[0]
            product_names.add(name)
        file_read.close()

        # Открываем файл для дозаписи новых продуктов
        file_append = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            if product.name not in product_names:
                file_append.write(f"{product}\n")
                product_names.add(product.name)
            else:
                print(f"Продукт {product.name} уже есть в магазине.")
        file_append.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
