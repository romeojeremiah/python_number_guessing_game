#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
from random_guess import computer_guess
import replit
play_game = True
play_again = True

while play_again == True:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        number_of_guesses = 10
    elif difficulty == "hard":
        number_of_guesses = 5

    print(f"You have {number_of_guesses} attempts remaining to guess the number.")


    while play_game == True and number_of_guesses != 0:
        guess = int(input("Make a guess: "))
        if guess != computer_guess:
            number_of_guesses -= 1
            if guess > computer_guess:
                replit.clear()
                print(f"You guessed {guess}. Too high.")
                print("Guess again.")
                print(f"You have {number_of_guesses} remaining to guess the number.")
                
            elif guess < computer_guess:
                replit.clear()
                print(f"You guessed {guess}. Too Low.")
                print("Guess again.")
                print(f"You have {number_of_guesses} remaining to guess the number.")
                
        else:
            play_game = False

    if guess == computer_guess:
        print(f"You guessed the number! It was {computer_guess}. You win! 🙂 ")
    else:
        print(f"You ran out of guesses. The number was {computer_guess}. You lose! 😖")

    try_again = input("Would you like to try again? 'y' or 'n' ")
    replit.clear()
    if try_again != 'y':
        play_again = False
    


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

