#Shopping cart program
item = input("what item would you like to buy ? ")
price = float(input("what is the price for it ? "))
quantity = int(input("How many would you like to buy ? "))
total = price * quantity
print(f"your bill is ${total}")