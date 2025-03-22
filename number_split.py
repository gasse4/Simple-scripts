def number_split(x):
    return [x/2,x/2] if x % 2 == 0 else [(x+1)/2,(x+1)/2-1]

y = int (input("Enter a number : "))
print(number_split(y))