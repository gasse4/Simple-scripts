x = int(input("Enter a decimal number: "))
octal = ""
while x > 0:
    octal = str(x % 8) + octal
    x = x // 8
print(f"The octal representation is {octal}")

y = int(input("Enter an octal number: "))
decimal = 0
i = 0
while y > 0:
    decimal += (y % 10) * 8 ** i
    y = y // 10
    i += 1
print(f"The decimal representation is {decimal}")
