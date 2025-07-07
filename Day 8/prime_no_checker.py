#prime number checker
#The nuber which is divisible by 1 and itself is called prime number

n = int(input("Check this number: "))

def prime_checker(number = n):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")    
prime_checker()
