from MyLib import *
num = i_input("Put the number: ")
string = str(num)
z = 0
if z == 0:
    for x in range(len(string)):
        for y in range(len(string)):
            if x != y and string[x] == string[y]:
                print("Not unique")
                z = 1 
                break
        if z == 1:
            break

if z == 0:
    print("Unique")
