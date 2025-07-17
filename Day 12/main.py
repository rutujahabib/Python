enemies = 1  #global scope

def increse_enemies():
    enemies = 2
    print("Enemies inside function:", {enemies})

increse_enemies()
print("Enemies outside function:", {enemies})

#local scope

def drink_potion():
    potion_strength = 2
    print("Potion strength inside function:", {potion_strength})

drink_potion()
print("Potion strength outside function:", {potion_strength})  # This will raise an error since potion_strength is not defined outside the function