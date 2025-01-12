questions = ("How many elements are there in peroiodic table ?",
             "which animal lays the largest eggs ?",
             "what's the most abundant gas in earth's atmosphere")
options = (("A.116","B.117","C.118","D.119"),
           ("A.whale","B.crocodile","C.elephant","D.ostrich"),
           ("A.nitrogen","B.oxygen","C.carbon-dioxide","D.hydrogen"), ())
answers = ("C","D","A")
guesses = []
score = 0
ques_num = 0

for question in questions:
    print("---------------------------------------")
    print(question)
    for option in options[ques_num]:
        print(option)
    guess = input("Enter (A, B, C, OR D) : ").upper()
    guesses.append(guess)
    if guess == answers[ques_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[ques_num]} is the correct answer")
    ques_num += 1