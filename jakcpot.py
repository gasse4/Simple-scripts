def jakcpot():
    list = [1,1,1,1]
    goal = 0
    for i in range(4):
        if list[0]==list[i] and i !=0:
            goal +=1
    if goal == 3:
        return "Jackpot"
    else:
        return "not jackpot"
print(jakcpot())

