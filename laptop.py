class Laptop():
    def __init__(self,brand,series,price,stock):
        self.__brand = brand
        self.__series = series
        self.__price = price
        self.__stock = stock
    
    # Getters
    def getBrand(self):
        return self.__brand

    def getSeries(self):
        return self.__series

    def getPrice(self):
        return self.__price

    def getStock(self):
        return self.__stock

    # Setters
    def setBrand(self, brand):
        self.__brand = brand

    def serSeries(self, series):
        self.__series = series

    def setPrice(self, price):
        self.__price = price

    def setStock(self, stock):
        self.__stock = stock

    def setSeries(self, series):
        self.__series = series

    
    # Get amount from user, update stock
    def bought(self, amount):
        self.__stock -= amount
    
    # Return the total price to user
    def total(self, amount):
        return amount * self.getPrice()