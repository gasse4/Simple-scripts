# MY FUNCTIONS

#Filtered function is  a function that return the true and abandoning the false
#filter(condition,list)

#sorted func is to arrange the values from the smaller to the longer

  
def i_input(prompt):
    return int(input(prompt))


########################################################################
########################################################################


def f_input(prompt):
    return float(input(prompt))


########################################################################
########################################################################


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


########################################################################
########################################################################


def get_portion_saved(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 1:
                print("Please enter a value between 0 and 1.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


########################################################################
########################################################################


def Fibonacci(n):
    if n < 0:
        print("Must be positive")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


########################################################################
########################################################################


def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        else:
            return True


########################################################################
########################################################################


def triangular():
    n = int(
        input(("Put the limit: "))) 
    total = 0
    for i in range(1, n):
        total += i
    return total


########################################################################
########################################################################


def sigma():
    n = int(input("Put the limit of the sum: "))
    Range = int(input("Put your range: "))
    coefficient = int(input("Put the coefficient "))
    if n < 0:
        print(f"Error: {n} Must be positive")
    else:
        Sum = 0
        for x in range(Range, n + 1):
            Sum += x
        Sum *= coefficient
        print(f"The sum from {Range} to {n} for {x} Num is: {Sum}")


########################################################################
########################################################################


def mysqrt(x):
    epsilon = 0.00000000000000000000000000001
    low = 0
    high = x
    answer = (high + low) / 2.0
    while abs(answer**2 - x) >= epsilon:
        if answer**2 < x:
            low = answer
        else:
            high = answer
        answer = (low + high) / 2.0
    return answer


########################################################################
########################################################################

def factorial(n):
    if n < 0:
        print("Must be positive")
        return None
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
########################################################################
########################################################################

def power(base, exp):
    return base ** exp


########################################################################
########################################################################

def is_even(num):
    return (num)% 2 == 0


########################################################################
########################################################################


def is_odd(num):
    return (num) % 2 != 0


########################################################################
########################################################################

def reverse(string):
    print(f"The reversed string is :{string[::-1]}")

########################################################################
########################################################################

def palindrome(string):
    while len(string)< 3:
        string = input("Enter a string that contains more than 2 characters")
    if string == string[::-1]:
            print("Palindrome")
    else:
            print("Not palindrome")
            
########################################################################
########################################################################

def Paragraph_check(wordy):
    
    wordy_c = wordy.count(".") + wordy.count("?") + wordy.count("!")
    s_sentence = wordy.replace("?",".").replace("!",".").split(".")

    punctuation_marks = [".","?","!",",",":",";","/"]
    for x in punctuation_marks:
        wordy = wordy.replace(x," ")

    set = wordy.split()
    word_count = 0
    for i in range(len(set)+1):
        word_count = i
    
    print("###################################################")
    print(f"the count of the words is : {word_count}")
    print("###################################################")
    print(f"The count of the sentences is : {wordy_c}")
    print("###################################################")
    print(f"The longest word in your string is: {(max(set, key=len))}")
    print("###################################################")
    print(f"The longest sentence in your string is: {(max(s_sentence, key=len))}")
    print("###################################################")
        
########################################################################
########################################################################
