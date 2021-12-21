from storage import *

def brandList():
    print("Here are some brands that we have in stock")
    print("1. lenovo")
    print("2. apple")
    print("3. hp")
    ans = eval(input("Enter the brand you want to purchase : "))
    # for i in range(len(laptop)):
    #     if(brand == laptop[i]):
    #         disSeries(brand)
    #     else:
    #         print("Sorry, we don't have the brand you want.")
    #         exit
    if ans == 1:
        disSeries(lenovo)
    elif ans == 2:
        disSeries(apple)
    elif ans == 3:
        disSeries(hp)
    else:
        print("Sorry, please enter the right number")
        print("___________________________")
        brandList()

def listing(brand):
    for i in range(len(brand)):
        print(f"{i+1}. {brand[i].getSeries().ljust(15)}${brand[i].getPrice()}")

def disSeries(brand):
    print("___________________________")
    print(f"For {brand[0].getBrand()} brand, we have:")
    listing(brand)
    ans = int(input("Enter the series you want to buy: "))
    # for i in range(len(brand)):
    #     if (brand[i].getSeries().casefold() == series):
    #         break
    #     else:
    #         print("Sorry, we don't have that series.")
    #         exit()
    if ans == 1:
        series = brand[0].getSeries()
    elif ans == 2:
        series = brand[1].getSeries()
    elif ans == 3:
        series = brand[2].getSeries()
    else:
        print("Sorry, please enter the right series")
        print("___________________________")
        disSeries(brand)
    amount = int(input("Enter the amount you want to purchase: "))
    if amount > 0:
        stockCheck(brand, series, amount)
    else:
        while True:
            print("Amount can't be less than 1")
            amount = int(input("Please enter the new amount: "))
            if amount > 0:
                break
        stockCheck(brand, series, amount)
            


def stockCheck(brand, series, amount):
    for i in range(len(brand)):
        if (brand[i].getSeries() == series):
            if amount > brand[i].getStock():
                print(f"Not enough in stock. There are currently {brand[i].getStock()} in stock.")
            else:
                brand[i].bought(amount)
                print("Confirmation:")
                print("BRAND    SERIES    TOTAL PRICE")
                print("==============================")
                print(f"{brand[i].getBrand()}   {brand[i].getSeries()}      ${brand[i].total(amount)}")
                conf = str(input("Confirm (yes/no)? "))
                if conf == "yes":
                    print("==============================")
                    print("Purchase successful!")
                    print("Thank you for using our service.")
                    print("See you next time!")
                else:
                    print("==============================")
                    print("Purchase failed.")
                    
            break
