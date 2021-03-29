from data import products

class MyMap:

    def __init__(self) -> None:
        self.products = products


    def show(self):
        return self.products
        

    def name(self):
        return list(map(lambda product: product['name'], self.products)) 


    def price(self):
        return list(map(lambda product: product['price'], self.products)) # para visualizar os dados no terminal é preciso converter em uma estrutura como Lista, por exemplo. 
       

    def kg(self):
        return list(map(lambda product: product['kg'], self.products)) 