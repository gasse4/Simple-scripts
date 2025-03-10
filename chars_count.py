def count_char():
    count = 0
    inpt = input("Enter your text here: ")
    inpt.split(" ")
    for elem in inpt:
        if elem != " ":
            count += 1
    print (count)
count_char()