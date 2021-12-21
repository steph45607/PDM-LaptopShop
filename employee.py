from storage import *

def main():
    ans = str(input("Do you want to make an update (y/n/check)? "))
    if(ans == "y"):
        brand = eval(input("Which brand do you want to update (lenovo/apple/hp)? "))
        update(brand)
    elif(ans == "check"):
        brand = eval(input("Which brand do you want to check (lenovo/apple/hp)? "))
        checking(brand)
    else:
        print("Thank you and have a great day!")

def checking(brand):
    print("BRAND          SERIES         PRICE")
    for i in range(len(brand)):
        print(f"{brand[i].getBrand().ljust(15)}{brand[i].getSeries().ljust(15)}${brand[i].getPrice()}")

def update(brand):
    print("SERIES            PRICE     STOCK")
    for i in range(len(brand)):
        print(f"{brand[i].getSeries().ljust(18)}${str(brand[i].getPrice()).ljust(9)}{brand[i].getStock()}")
    series = eval(input("Enter which series to update: ")).casefold()
    updating = eval(input("What do you want to update (price/stock)? "))
    for i in range(len(brand)):
        if (brand[i].getSeries().casefold() == series):
            if(updating == "price"):
                newPrice = int(input("Enter new price: "))
                series.setPrice(newPrice)
            elif(updating == "stock"):
                newStock = int(input("Enter stock added:"))
                series.setStock(newStock)
        else:
            print("Sorry, please enter the right series.")
            

