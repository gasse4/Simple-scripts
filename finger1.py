from MyLib import*
n = i_input("Enter the number: ")
i = 0
while i**3 < n:
    i+=1
if i**3 == n:
    print(i)
else:
    print("error")