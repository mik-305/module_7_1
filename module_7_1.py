import io
from pprint import pprint
class Product:
    global products
    products = ''
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = str(weight)
        self.category = category
    def __str__(self):
        products = self.name+', '+ self.weight+', ' +self.category
        return products

class Shop():
    def get_products(self):
        file = open('products.txt', 'r', encoding='utf-8')
        soder_file = file.read()                            # Содержимое файла
        file.close()
        return soder_file
    def add(self, *products):                               # Добавление продуктов в файл если их там нет
        file = open('products.txt', 'a', encoding='utf-8')
        in_magazin = self.get_products()
        i = 0
        while i < len(products):
            if products[i].name in in_magazin:
                print(f'Продукт {products[i]} уже есть в магазине')
            else:
                file.write(str(products[i]) + '\n')
            i += 1
        file.close()
#--------------------------------------------------------------------------------------------------------
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


