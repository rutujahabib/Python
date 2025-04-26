print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
tip = int(tip)  # Convert the input to an integer
people = int(people)  # Convert the input to an integer
bill = float(bill)  # Convert the input to a float
percent = tip/100
total_tip = bill * percent  # Calculate the total tip
total_bill = bill + total_tip  # Calculate the total bill including tip
amount_per_person = round((total_bill / people), 2)  # Calculate the amount each person should pay, rounded to 2 decimal places
print(f"Each person should pay: ${amount_per_person}")
