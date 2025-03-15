def NOT(prompt):
    return int(not prompt)

#####################################################################
def AND(prompt_1, prompt_2):
        if not (0 <= prompt_1 <= 1) or not (0 <= prompt_2 <= 1):
            return "Invalid input, please put (0 or 1)"
        elif prompt_1 == prompt_2 !=0 :
            return 0
        else:
            return 1
#####################################################################

def OR(prompt_1, prompt_2):
        if not (0 <= prompt_1 <= 1) or not (0 <= prompt_2 <= 1):
            return "Invalid input, please put (0 or 1)"
        elif prompt_1 == 1 or prompt_2 == 1:
            return 1
        else:
            return 0
#####################################################################

def NAND(prompt_1, prompt_2):
    if not (0 <= prompt_1 <= 1) or not (0 <= prompt_2 <= 1):
        return "Invalid input, please put (0 or 1)"
    elif prompt_1 == 0 or prompt_2 ==0 or prompt_1 == prompt_2 !=1:
        return 1
    else:
        return 0
####################################################################

# def OR(prompt_1, prompt_2):
#         if not (0 <= prompt_1 <= 1) or not (0 <= prompt_2 <= 1):
#             return "Invalid input, please put (0 or 1)"
#         elif prompt_1 == 1 or prompt_2 == 1:
#             return 0
#         else:
#             return 1