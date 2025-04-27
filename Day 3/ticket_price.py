# conditional stmt, logical operators, code blocks and scopes 
#{if condtion:
#    do this
#else:
#    do that}

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 12
        print("Please pay $12.")
    elif age <= 18:
        bill = 7
        print("Please pay 7.")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")   
    else:
        bill = 15
        print("Please pay $15.")

    wants_photo= input("Do you want a photo taken? yes or no? ")   
    if wants_photo == "yes":
        bill += 3   
    print(f"Your final ticket bill is ${bill}.")
      
else:
    print("Sorry, you can't ride the rollercoaster!")