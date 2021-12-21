from laptop import Laptop

class Order(Laptop):
    def __init__(self, brand, series):
        super().__init__(brand, series, price, stock)
        self.__price = self.getPrice()
        self.__stock = self.getStock()
    
    