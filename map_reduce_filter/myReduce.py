from data import products
from functools import reduce

class MyReduce: 
    def __init__(self):
        self.products = products

    def total_price(self):
        return reduce(lambda soma, product: soma + product['price'], self.products, 0)

    def total_kg(self):
        return reduce(lambda soma, product: soma + product['kg'], self.products, 0)
