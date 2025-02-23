from random import*
from termcolor import*
import pyfiglet
def name(s):
    if s == 1: 
        return("Rock")
    elif s == 2 :
        return("Scissors")
    else :
        return("Paper")

rounds = 3

global u_points
global cpu_points

u_points = 0
cpu_points = 0

rounds = int(input("Please,Enter the number of rounds (enter for def value 3) : ")) 
print("\n")

if  rounds % 2 == 0:
    rounds +=1
    
def Check_game(choice,cpu_choice):
    global u_points
    global cpu_points
    
    if (choice == 1 and cpu_choice == 2)or (choice == 2 and cpu_choice == 3) or (choice == 3 and cpu_choice == 1):
        u_points =u_points+ 1
        print("User's points =",u_points)
        prt1=("User win this round","\n",name(cpu_choice))
        print(colored(prt1,'green'))
    elif(choice==cpu_choice):
        print("Tie !", name(cpu_choice))
    else:
        cpu_points =cpu_points+ 1
        print("Cpu's points =",cpu_points)
        prt2=("CPU win this round\n", name(cpu_choice))
        print(colored(prt2,'red'))

def end_game(x,y):
    while True:
        if x > y:
            print(colored("User wins!\n",'light_magenta'))
            break
        elif x < y:
            print(colored("Cpu wins\n",'light_red'))
            break
        else:
            print("It is a tie\nThere is another try!\n")
            start_user_game(1)
            break
        
def start_user_game(rounds):
    cpu_choice = 0
    for i in range(rounds):
        choice = int(input("Enter '1'for ROCK or '2'for SCISSORS or '3'for Paper : "))
        while True:
            if  choice > 3 or choice <=0 :
                choice = int(input("Please,Enter a value between (1 , 3): "))
            else:
                break
        cpu_choice = randint(1,3)
        
        Check_game(choice,cpu_choice)
    end_game(u_points,cpu_points)   
    
    return rounds

start_user_game(rounds)

txt=pyfiglet.figlet_format(f"Final Score: ")
print(colored(txt,'light_yellow'))
print(f"\nCPU: {cpu_points}\nUSER: {u_points}")