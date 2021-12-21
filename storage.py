from laptop import Laptop

x270 = Laptop("Lenovo", "x270", 499, 10)
x280 = Laptop("Lenovo", "x280", 550, 8)
x1 = Laptop("Lenovo", "x1", 1500, 6)

air = Laptop("Apple", "Macbook Air", 999, 5)
pro13 = Laptop("Apple", "Macbook Pro 13", 1299, 5)
pro16 = Laptop("Apple", "Macbook Pro 16", 2499, 3)

spectre = Laptop("HP", "Spectre x360", 1299, 6)
envy = Laptop("HP", "Envy 13", 1099, 7)
elite = Laptop("HP", "Elitebook x360", 2350, 5)

lenovo = [x270, x280, x1]
apple = [air, pro13, pro16]
hp = [spectre, envy, elite]

# laptop = [lenovo, apple, hp]