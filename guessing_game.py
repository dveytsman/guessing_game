from random import randint
from replit import clear

print("Welcome to the number guessing game!")
print("")
def play_again():
    '''the function that asks the user if they want to play another round and returns True or False'''
    play = input("Would you like to play a round? y or n\n")
    if play == "y":
        play = True
    else:
        play = False
    return play

def play_game():
    '''this function runs one round of the game'''
    clear()
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    guess = 110
    mode = input("Would you like to try easy or hard mode? please type easy or hard\n")
    if mode == "easy":
        guesses = 10
    elif mode == "hard":
        guesses = 5
    while guess != answer and guesses > 0:
        if guesses == 1:
            keyword = "attempt"
        elif guesses > 1:
            keyword = "attempts"
        print(f"you have {guesses} {keyword} remaining")
        guess = int(input("Make a guess: "))
        if guess > answer:
            guesses -= 1
            if guesses == 0:
                print("You've Lost")
            else:
                print("Too high! Guess again")
        elif guess < answer:
            guesses -= 1
            if guesses == 0:
                print("You've Lost")
            else:
                print("Too Low! Guess Again.")
            
        else:
            print(f"You got the number, your guess: {guess} is secret number: {answer}")

while play_again():
    play_game()