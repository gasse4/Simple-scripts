def OR(prompt_1, prompt_2):
        if not (0 <= prompt_1 <= 1) or not (0 <= prompt_2 <= 1):
            return "Invalid input, please put (0 or 1)"
        elif prompt_1 == 1 or prompt_2 == 1:
            return 1
        else:
            return 0

inpt_1 = int(input("Enter the first value: "))
inpt_2 = int(input("Enter the second value: "))
print(OR(inpt_1,inpt_2))