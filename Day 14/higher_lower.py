from art import logo, vs
from game_data import data
import random
import os



def format_data(account):
    """Format the account data into printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."

def check_answer(guess, a_follower_count, b_follower_count):
    """Check if the user's guess is correct."""
    if a_follower_count > b_follower_count:
        return guess == 'A'
    else:       
        return guess == 'B'

print(logo)
score = 0   
game_should_continue = True 
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a) }")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for a fresh display

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")    
        game_should_continue = False

    