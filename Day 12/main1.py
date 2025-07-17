'''
enemies = 1 # global scope

def increse_enemies():
    global enemies  # Declare that we are using the global variable
    enemies += 1
    print("Enemies inside function:", {enemies})

increse_enemies()
print("Enemies outside function:", {enemies})  # This will raise an error since enemies   
'''

pi = 3.14  # global scope
URL = "https://www.google.com"  # global scope
TWiITTER_HANDLE = "@codewithtimmy"  
