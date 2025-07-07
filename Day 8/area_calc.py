import math

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5 # 5 square meters per can of paint

def paint_calc(height=test_h, width=test_w, cover=coverage):
    area = height * width
    no_of_cans = math.ceil(area / cover)
    print(f"You'll need {no_of_cans} cans of paint.")
paint_calc()    