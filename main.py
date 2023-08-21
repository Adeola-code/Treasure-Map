#Initial Rows on the map

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#The first digit in the input will specify the column (the position on the horizontal axis).
#The second digit in the input will specify the row number (the position on the vertical axis). 

#Logic
position=str(position)
column=position[0]
column=int(column)
row=position[1]
row=int(row)
map[row-1][column-1]="X"

#Final output
print(f"{row1}\n{row2}\n{row3}")

