def pentagonal(prompt):
    if prompt == 1 :
        return 1
    else:
        return pentagonal(prompt - 1) + 5 * (prompt - 1)
    
inpt = int(input("Enter a number : "))
print(pentagonal(inpt))
