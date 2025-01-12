# List comprehension : A concise way to create lists in python

# Traditional method
# doubles = []
# for x in range(1,11):
#         doubles.append(x * 2)
# print(doubles)


# List Comprehension method
# doubles = [x * 2 for x in range (1, 11)]
# triples = [x * 3 for x in range (1, 11)]
# squares = [x * x for x in range (1, 11)]
# print(squares)


# fruits =["Apple", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)


numbers = [1, 2, -7, -8, 5, 0, 8]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= -1]
odd_nums = [num for num in numbers if num % 2 != 0]
print(odd_nums)