foods = []
prices = []
total = 0
while True:
     food = input("Enter a food to buy(q to quit): ")
     if food.lower()  == "q": #upper case Q k liye
        break
     else:
         price = float(input(f"enter price of {food}: $"))
         foods.append(food)
         prices.append(price)
         
print("..YOUR CART..")

for food in foods:
        print(food, end=" ")
        # end=" " - same line me likhne k liye with spaces " "
        
for price in prices:
    total += price
print()
print(f"your total is : ${price}")