def same():
    count=0
    list = ['x','y','x','x','x','j','x']
    for x in range(len(list)):
        if list[0]== list[x]:
            count +=1 
    print(count)
        
same()