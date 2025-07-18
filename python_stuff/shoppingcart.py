print("Welcome to the fruit and vegetable shop!")
print("*" * 25)
fruits = { "apple": 0.2, "banana": 5, "orange": 6, "kiwi": 7, "mango": 0.8, "peach": 0.9 }
veggies = { "carrot": 3, "broccoli": 0.4, "spinach": 5, "potato": 0.6, "onion": 7 }
basket = []

for fruit in fruits:
    print("fruits available: ", fruit)

for veggy in veggies:
    print("veggies available: ", veggy)


while True:
    product1 = input("Enter the name of the fruit: ")
    product2 = input("Enter the name of the veggy: ")

    if product1 not in fruits:
        print(f"{product1} is not a valid fruit.")
        continue
        
    elif product2 not in veggies:
        print(f"{product2} is not a valid vegetable.")
        continue
    else:    
        print("****YOUR good to go****") 
        break

print(f"How many {product1}s do you want?")
print(f"How many {product2}s do you want?")

total_fruits = int(input(" > "))
total_veggies = int(input(" > "))

basket.append(f"{total_fruits} * {product1}")
basket.append(f"{total_veggies} * {product2}")

if basket:
    print("You have added the following items to your basket:")
    for products in basket:
        print(f"* {products}")

call = input("Do you want to calculate the total price? (yes/no): ")

if call == "yes":
    def amount():
        prices = (fruits[product1] * total_fruits) + (veggies[product2] * total_veggies)
        return prices
    prices = amount()
    if prices > 50:
        print("You have a discount of 30% on your total price!")
        discount_precentage = 30
        price = prices * (discount_precentage / 100)
        print(f"The price for {total_fruits} {product1} is ${fruits[product1] * total_fruits: .2f}")
        print(f"The price for {total_veggies} {product2} is ${veggies[product2] * total_veggies: .2f}")
        print(f"Items bought are {total_fruits} {product1} and {total_veggies} {product2}")
        print(f"Your total price is: ${prices:.2f}")
        print(f"Your discounted amount is: ${prices - price:.2f}")
        print("Thank you for visiting the fruit and vegetable shop!")
        print("*" * 25)
    elif prices > 10:
        print("You have a discount of 10% on your total price!")
        discount_precentage = 10
        price = prices * (discount_precentage / 100)
        print(f"The price for {total_fruits} {product1} is ${fruits[product1] * total_fruits: .2f}")
        print(f"The price for {total_veggies} {product2} is ${veggies[product2] * total_veggies: .2f}")
        print(f"Items bought are {total_fruits} {product1} and {total_veggies} {product2}")
        print(f"Your total price is: ${prices:.2f}")
        print(f"Your discounted amount is: ${prices - price:.2f}")
        print("Thank you for visiting the fruit and vegetable shop!")
        print("*" * 25)
    else:
        print(f"The price for {total_fruits} {product1} is ${fruits[product1] * total_fruits: .2f}")
        print(f"The price for {total_veggies} {product2} is ${veggies[product2] * total_veggies: .2f}")
        print(f"Items bought {total_fruits} {product1} and {total_veggies} {product2}")
        print(f"Your total price is: ${prices:.2f}")
        
else:
    print("Thank you for visiting the fruit and vegetable shop!")
    print("*" * 25)
    print("Have a great day!")




