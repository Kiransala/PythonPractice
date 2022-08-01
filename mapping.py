row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) #hold the first digit of input
vertical = int(position[1])   #hold the second digit of input

#first go to verical row inside vertical it go horizontal row
map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")