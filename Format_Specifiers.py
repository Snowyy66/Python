# format specifiers = {value:flag} format a value based on what flags are inserted

#(number)f = round to that many decimal places (fixed point)
#: (number) = allocate that many spaces
#:03 = allocate and zero pad that many spaces
#:<= left justify
#:> = right justify
#:^ = center align
#:+ = use a plus sign to indicate positive value
#:= = place sign to leftmost position
#: = insert a space before positive numbers

price1 = 4.588
price2 = -4.588
price3 = 4563.9748
# print(f"price is ${price1:.2f}")
# print(f"price is ${price1:10}") # 10 spaces
# print(f"price is ${price1:010}")
# print(f"price is ${price1:<10}") 
# print(f"price is ${price1:^10}") # center
# print(f"price is ${price1:+}")
# print(f"price is ${price2:+}")
# print(f"price is ${price3:,}") #put comma after digit 1
print(f"price is ${price3:+,.2f}")
