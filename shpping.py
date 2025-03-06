#Exercise 1 Shopping Cart program
item = input("What item would you like to buy: ")
price = float(input("What is the price of : "))
quantity = int(input("How much would you like to have?: "))
total = price * quantity

print(f"Your total is {quantity} X {item}/s")
print(f"Your total is ${total}")
