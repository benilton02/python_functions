from data import products

class MyFilter():

    def __init__(self):
        self.products = products

    def show(self):
        """Retorna um objeto filter."""
        return filter(lambda produc: True, self.products)

    def price(self):
        """Retorna os produtos acima de 90"""
        return list(filter(lambda product: product['price'] > 90, self.products ))

    def kg(self):
        """Retorna os produtos acima de 1.5kg"""
        return list(filter(lambda kg: kg['kg'] > 1.5, self.products))
    
