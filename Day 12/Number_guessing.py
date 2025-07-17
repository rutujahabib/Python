import random
from art import logo

def play_game():
    print(logo)
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    attempts = 0    

    level_choice = input("Choose a difficulty level (easy/hard): ").lower()
    max_attempts = 10 if level_choice == 'easy' else 5

    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        if guess < number_to_guess:
            print("Too low. Guess again.")
        elif guess > number_to_guess:
            print("Too high. Guess again.")
        else:
            print(f"🎉 Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

        print(f"You have {max_attempts - attempts} attempts left.\n")

    else:
        print(f"😢 Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Run the game
play_game()
