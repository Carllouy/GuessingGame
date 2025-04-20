#Carl Louy, CIS261, Guessing Game
import random

def numberGuess():
    randomNumber = random.randrange(1,11)
    guess = int(input("Try to guess the number:"))
    print (randomNumber)
    while True:
        if (guess == randomNumber):
            print ("Thats Right")
            break
        if (guess > randomNumber):
            print ("Incorrect, your guess was too high")
            guess = int(input("Try to guess the number:")) 
            print ("Incorrect, your guess was too low")
            guess = int(input("try to guess the number:"))
            
numberGuess()