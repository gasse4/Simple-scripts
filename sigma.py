def sigma():
    n = int(input("Put the limit of the sum: "))
    Range = int(input("Put your range: "))
    coefficient = int(input("Put the coefficient "))
    if n < 0:
        print(f"Error: {n} Must be positive")
    else:
        Sum = 0
        for x in range(Range, n + 1):
            Sum += x
        Sum *= coefficient
        print(f"The sum from {Range} to {n} for {x} Num is: {Sum}")

print(sigma())
