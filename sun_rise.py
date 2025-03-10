Degree = float(input("Enter the Degree: "))
if Degree < 0:
    Degree += 360
hours= ((Degree/15)+6)
if hours > 18:
    print("I can't see the sun")
else:
    print(f"The time is:{hours:.1f} ")