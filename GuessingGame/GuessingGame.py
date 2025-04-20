#Carl Louy, CIS261, Guessing Game

import random

def display_Heading():
    print("=====================================")
    print("  Guess The Number")
    print("=====================================")
    

def play_Game(limit):
    number_to_guess = random.randint(1, limit)
    print(f"I am thinking of a number between 1 and {limit}.")
    
    while True:
        try:    
            guess = int(input("Take a guess: "))
            if guess < number_to_guess:
                print("Too Low. Take another Guess")
            elif guess > number_to_guess:
                print("Too High. Take another Guess")
                break
        except ValueError:    
            print("Please enter a valid number")
    
def main():
    display_Heading()
    
while True:
    try:
        limit = int(input("Enter the higest number for your guessing range: "))
        if limit < 1:
            print("Enter a number greater than 0.")
            continue
        play_Game(limit)
    except ValueError:
        print("Enter a valid number.")
        continue
    play_again = input("Play again? (yes/no): ").strip().lower()
if play_again != 'yes':
    print("Good bye")

if __name__ == "__main__":
    main()
