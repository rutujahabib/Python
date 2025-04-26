age =input("what is your current age? ")    
age = int(age)  # Convert the input to an integer
years_remaining = 90 - age  # Calculate the years remaining until 90
days_remaining = years_remaining * 365  # Calculate the days remaining
weeks_remaining = years_remaining * 52  # Calculate the weeks remaining
months_remaining = years_remaining * 12  # Calculate the months remaining
print(f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, and {years_remaining} years left until you turn 90.")
