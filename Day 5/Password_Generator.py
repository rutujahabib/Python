import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator!")
nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input("How many symbols would you like?\n")
nr_numbers = input("How many numbers would you like?\n")

password_list = []

for char in range(1, int(nr_letters) + 1):
  password_list += random.choice(letters)

for char in range(1, int(nr_symbols) + 1):
    password_list += random.choice(symbols)

for char in range(1, int(nr_numbers) + 1):
   password_list += random.choice(numbers)
print(f"Your password is:{password_list}")

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
