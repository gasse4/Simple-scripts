def AND(prompt_1, prompt_2):
        if not (0 <= prompt_1 <= 1) or not (0 <= prompt_2 <= 1):
            return "Invalid input, please put (0 or 1)"
        elif prompt_1 ==0 or prompt_2 ==0 :
            return 0
        else:
            return 1

inpt_1 = int(input("Enter the first value: "))
inpt_2 = int(input("Enter the second value: "))
print (AND(inpt_1,inpt_2))