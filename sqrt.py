from Scripts.MyLib import i_input
def mysqrt(x):
    epsilon = 0.00000000000000000000000000001
    low = 0
    high = x
    answer = (high + low)/2.0
    while abs(answer**2 - x)>=epsilon:
        if answer**2 < x:
            low = answer
        else:
            high = answer
        answer = (low + high)/2.0
    return answer
y = i_input("put the number: ")
print (mysqrt(y))