points,status = 0,["Wins", "Draws", "Losses"]
for x in status:
    multiplier = 3 if x == "Wins" else 1 if x == "Draws" else 0 
    z = int(input(f"Enter the number of {x}: "))
    points += z * multiplier
print(f"Total Points: {points}")

