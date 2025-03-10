def remove_num():
    limit = int(input("Enter the limit: "))
    lst = []
    for i in range(limit):
        inpt = int (input(f"enter the element {i+1} of a list "))
        lst.append(inpt)
    print("Your list is: \n",lst)
    rmv=int(input("Enter the number you want to remove: "))
    while True :
        for x in lst :
            if rmv in lst :
                lst.remove(rmv)
        break
    print(lst)
remove_num()