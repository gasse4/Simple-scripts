from termcolor import colored
import pyfiglet

def validation(subject):
    min,max=0,100
    while True:
        if subject< min or subject >max:
            subject = int(input("Please,enter avalue between (0,100): "))
        else:
            break
    return subject
            
def grade(score):
    if score >=90 and score <=100:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
    
def average(score,limit):
    var = sum(score)
    avg = var/limit
    return avg

def GPA_calc(grade):
    if grade =="A":
        return 4.0
    elif grade =="B":
        return 3.0
    elif grade =="C":
        return 2.0
    elif grade =="D":
        return 1.0
    elif grade =="F":
        return 0.0
    
text = colored("Welcome to our calculator\nPlease enter your scores: ", 'green') 
print(text)
limit = int(input("Enter the number of your subjects: "))
while True:
    if limit < 2:
        limit = int(input("Enter a number(that is bigger than 2): "))
    else:
        break
    
sub = 1
score = []
for i in range(limit):
    total = (int(input(colored(f"Enter test score {sub}: ",'light_cyan','on_black')))) 
    validated_score =  validation(total)
    sub+=1
    score.append(validated_score)
    
gpa = GPA_calc(grade(average(score,limit)))
print(colored(f"The average score is:{average(score,limit):.4f}\nThe letter grade is:{grade(average(score,limit))}",'black'))
print(colored(f"Your gpa is {gpa}",'light_yellow'))


text1 = pyfiglet.figlet_format("Best wishes")
print(text1)