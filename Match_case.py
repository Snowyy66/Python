# MATCH-CASE(SWITCH CASE)

# def day_of_week(day):
#     match day:
#         case 1:
#             return "it's sunday!"
#         case 2:
#             return "it's monday!"
#         case 3:
#             return "it's tuesday!"
#         case 4:
#             return "it's wednesday!"
#         case 5:
#             return "it's thursday!"
#         case 6:
#             return "it's friday!"
#         case 7:
#             return "it's saturday!"
#         case _:
#             return "Not a valid day!"
# print(day_of_week(7))
 
 
        
# Another Example   
def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(is_weekend("Sunday"))
