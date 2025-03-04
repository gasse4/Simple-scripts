from termcolor import *
def pass_validation(password):
    signs = ["#","@","!","$","%","&","*"]
    strength = 0
    while True:
        if len(password) < 8:
            password = input("Password should be >= 8 characters\n")
            continue
        elif not any(char.isalpha() for char in password):
            password = input("Password should be contained with at least one character\n") 
            continue
        elif not any(sign in password for sign in signs):
            password = input("Password should be contained with special characters like (@,!,#,&)\n")
            continue
        elif not any(char.isdigit() for char in password):
            password = input("Password should be contained with at least one number\n")
            continue
        else:
            break
    if len(password) >= 10:
        strength +=1
    if any(char.isalpha() for char in password):
        strength +=1
    if any(sign in password for sign in signs):
        strength +=1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        strength +=1
    
    if strength <=2:
        print(colored("Password is weak!",'red'))
    elif strength == 3:
        print(colored("Password is medium",'light_yellow'))
    else :
        print(colored("Password is strong",'green'))
    
            
           
password = input("Enter your password:\n")
pass_validation(password)