row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure?")  #23

horizontal = int(position[0])  #2
vertical = int(position[1])   #3

map[vertical - 1][horizontal -1] = "X" #= map[3 - 1][2 - 1]

print(f"{row1}\n{row2}\n{row3}")