import random
low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True
print("...NUMBER GUESSING GAME !...")
print(f"select a number between {low_num} & {high_num}")

while is_running:
    
    guess = input("Enter your guess : ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < low_num or guess > high_num:
            print("The number is out of range")
            print(f"select a number between {low_num} and {high_num}")
        elif guess < answer:
            print("Too low ! try again")
        elif guess > answer:
            print("Too high ! try again")
        else:
            print(f"Correct ! the answer was {answer}")
            print(f"Number of guesses : {guesses}")
            # is_running = False
    else:
        print("Invalid guess")
        print(f"select a number between {low_num} and {high_num}")
