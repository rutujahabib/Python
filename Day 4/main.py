#randomisation and python lists
#Module- split code into multiple modules

import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

random_float = round(random.random()*5, 3)
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
print(my_module.pi)