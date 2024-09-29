import io
from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = str(weight)
        self.category = category
    def __str__(self):
        return self.name + ', ' + self.weight + ', ' + self.category

class Shop:
    def get_products(self):
        file = open('products.txt', 'r', encoding='utf-8')
        pprint(file.read())
        file.close()

s1 = Shop()
print(s1.get_products())

p1 = Product('Potato', 50.5, 'Vegetables')
print(str(p1))
p2 = Product('Spaghetti', 3.4, 'Groceries')
print(str(p2))


