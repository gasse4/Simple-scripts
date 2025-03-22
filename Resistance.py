def R(*args):
    total = 0
    for arg in args:
         total += arg
    return total

print(R(5,10,15,20))