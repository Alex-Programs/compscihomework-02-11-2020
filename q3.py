# 3.	There are two monkeys called A and B.  Ask the keeper if each monkey is smiling (you will have to ask two separate questions, i.e. is monkey A smiling, is monkey B smiling). If both monkeys are smiling then the keeper must be afraid as the monkeys are plotting something and you must tell the keeper it is not safe to enter the cage. If neither monkey is smiling then the keeper must also be afraid as the monkeys are angry at something and you must tell them it is not safe to enter the cage. If one monkey is smiling and the other isn’t smiling then you can tell the keeper it is safe to enter the cage.

while True:
    #Get input. I'm not sure about inline formatting, if this was a bigger project I'd put it into a function.
    isASmiling = False
    if (input("Is A smiling? Enter Y/N: ").upper().replace(" ", "") == "Y"):
        isASmiling = True

    isBSmiling = False
    if (input("Is B smiling? Enter Y/N: ").upper().replace(" ", "") == "Y"):
        isBSmiling = True

    # a simple if statement would be better here in this circumstance, but I read about this trick in JS where you can add truthy values to get a sum.
    # Python is sane so this won't impact it too much, but I might as well do it anyway. 

    _sum = 0

    if isASmiling:
        _sum += 1
    if isBSmiling:
        _sum += 1

    if _sum == 2:
        print("They're up to something, don't go in.")
    elif _sum == 1:
        print("It's safe.")
    else:
        print("Don't go in, they're angry.")