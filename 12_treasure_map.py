# Simple mapping game utilizing lists and nested lists

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter your answer as column number then row number eg '23': ")


vertical = int(position[0])
horizontal = int(position[1])

map[horizontal - 1][vertical - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")