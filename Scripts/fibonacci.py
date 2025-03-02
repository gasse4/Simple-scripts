n = int(input("Put the limit of the numbers: "))
n0,n1 = 0,1
f = n1
count = 1
print(f"{n0}\n{n1}")
while count <= n:
    print(f"{f}")
    count += 1
    n0 = n1
    n1 = f
    f = n0 + n1
