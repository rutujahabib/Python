#dictionaries and nesting
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Loop"])

programming_dictionary["Loop"] = "The action of doing something repeatedly until a condition is met."

print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
