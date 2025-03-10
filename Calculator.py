class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self,num1,num2):
        return num1 + num2

    def sub(self,num1,num2):
        return num1 - num2

    def mult(self,num1,num2):
        return num1*num2

    def div(self,num1,num2):
        while True:
            if num2 == 0:
                print("Error! num2 must not = 0")
            else:
                return num1/num2


numb1 = float(input("Put the number 1: "))
numb2 = float(input("Put the number 2: "))

Calc = Calculator(numb1,numb2)

print ("The addition is ",Calc.add(numb1,numb2))
print ("The subtraction is ",Calc.sub(numb1,numb2))
print ("The multiplication is ",Calc.mult(numb1,numb2))
print ("The division is ",Calc.div(numb1,numb2))




