# 2.	Write a program that asks a multiple choice question.  If they get the answer correct then display “Well done”; if they get the answer wrong then display “Try again” and they repeat the question until they get it right.

#set vars
answer = "blue"
correct = False
possibleAnswers = ["blue", "red", "green", "yellow"]

#mainloop
while correct == False:
    print("\nWhat is the best colour? Choices are red, blue, green, yellow:")

    choice = input("> ")

    #remove spaces
    formattedChoice = choice.replace(" ", "").lower()

    #check if answer is valid
    if formattedChoice in possibleAnswers:
        #if valid, check if correct
        if formattedChoice == answer:
            print("Correct!")
            correct = True

        else:
            print("That answer is a valid choice, but the wrong choice.")
    
    else:
        print("Hmm, that answer isn't valid. Did you spell it right?")