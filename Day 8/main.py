#functions with inputs
#caeser Cipher
#arhumensts and parameters

#def greet():
    #print("Hello")
    #print("Welcome to the Caesar Cipher program!")
    #print("Isnt the weather nice today?")
#greet()   

#def greet_with_name(name):
    #print(f"Hello {name}")
    #print(f"Welcome to the Caesar Cipher program {name}!")
    #print("Isnt the weather nice today?")
#greet_with_name("rutuja")   

#function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Welcome to the Caesar Cipher program {name}!")
    print(f"Isnt the weather nice today in {location}?")
#greet_with("rutuja", "pune")  ----position arguments    

#functions with keyword arguments
greet_with(name="rutuja", location="pune") 