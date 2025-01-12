# keyword arguments =  arguments prefixed with the names of parameters
#                      order of the arguments doesn’t matter,
#                      helps with readability
#                      order of argument doesn't matter
#                      1. positional, 2. DEFAULT 3. keyword 4. arbitrary



# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")
    
# hello("Good Morning", "Mr", "Ashish", "sisodiya")


#Example
# for x in range(1, 11):
#     print(x, end=" ")



#Example 2
# print("1","2","3","4","5",sep="-")


#Example 3
def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1,area=123,first=456,last=789)
print(phone_num)
