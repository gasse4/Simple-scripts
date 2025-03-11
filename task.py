def get_pair():
    num = []
    lim = int (input("Enter the length of the list: "))
    for y in range(lim):
        inpt = int(input(f"Enter the element {y} of the list: "))
        num.append(inpt)
    print(num)
    value = int(input("Enter the value to get the pair of numbers: "))
    for i in num:
        for x in num:
            if i + x == value :
                print(f"{i,x}")
            if i == x:
                break

get_pair()
