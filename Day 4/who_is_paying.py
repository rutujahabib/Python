import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

#split string method
nameAsCSV = input("Give me everybody's names, separated by a comma. ")
names = nameAsCSV.split(", ")

print(names)

num_items = len(names)
random_choice = random.randint(0,  num_items - 1)

person_who_will_pay = names[random_choice]
# person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")