arr = []
n = int(input("How many elements do you want to input? "))

for i in range(n):
    value = int(input(f"Enter value for element {i+1}: "))
    arr.append(value)
target = int(input("Put your target: "))

for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            print(f"{arr[i], arr[j]}")
