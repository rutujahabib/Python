from random import randint

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(guess, answer):
    if guess < answer:
        return "Too low. Guess again."
    elif guess > answer:
        return "Too high. Guess again."
    else:
        print(f"🎉 Congratulations! You've guessed the number {answer}.")

def set_difficulty():
    level_choice = input("Choose a difficulty level (easy/hard): ").lower()
    if level_choice == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

turns = set_difficulty()
print(f"You have {turns} attempts to guess the number.")

guess = int(input("Make a guess: "))

check_answer(guess, answer)
