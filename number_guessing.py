#Gregory Clarke
#Computer Programming
#9/25/2017


import random
x=random.randrange(1,11)
    

def numberguessing(x):

    y=int(input("Guess a number between 1 and 10?:"))

    if x==y:
        print("You guessed the number")

    else:
        print("You are wrong.")
        numberguessing(x)

numberguessing(x)



