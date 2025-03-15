def lists_n():
    largest = 0
    new_list=[]
    lists = [[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]
    for i in range(len(lists)):       
        for x in lists[i]:
            if x > largest:
                largest = x
        new_list.append(largest)
        largest = 0
    return new_list    
    
print(lists_n())