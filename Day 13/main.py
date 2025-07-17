#debugging
#def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("Reached 20")
# my_function()

# from random import randint
# dice_imgs = ["1","2","3","4","5","6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# year = int(input("Enter a birth year: "))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# age = int(input("how old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

#print your friend
# pages = 0
# word_per_page = 0
# pages = int(input("How many pages are in the book? "))
# word_per_page = int(input("How many words are on each page? ")) 
# total_words = pages * word_per_page
# print(f"The book has {total_words} words in total.")

#Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1, 2, 3, 5, 8, 13])    