def start():
    
    print("Welcome to the Units Converter")
    print("""1. Length
2. Volume
3. Weight
4. Temperature
5. Area
6. Speed
7. Time
8. Pressure
9. Power
10. Energy
11. Quit""")
        
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        user_input = float(input("Enter the length in meters: "))
        length(user_input)
    elif choice == 2:
        user_input = float(input("Enter the volume in liters: "))
        volume(user_input)
    elif choice == 3:
        user_input = float(input("Enter the weight in grams: "))
        weight(user_input)
    elif choice == 4:
        user_input = float(input("Enter the temperature in Celsius: "))
        temperature(user_input)
    elif choice == 5:
        user_input = float(input("Enter the area in square meters: "))
        area(user_input)
    elif choice == 6:
        user_input = float(input("Enter the speed in meters per second: "))
        speed(user_input)
    elif choice == 7:
        user_input = float(input("Enter the time in seconds: "))
        time(user_input)
    elif choice == 8:
        user_input = float(input("Enter the pressure in atm: "))
        pressure(user_input)
    elif choice == 9:
        user_input = float(input("Enter the power in watts: "))
        power(user_input)
    elif choice == 10:
        user_input = float(input("Enter the energy in joules: "))
        energy(user_input)
    elif choice == 11:
        print("Thank you for using the Unit Converter!")
            
    else:
        print("Invalid Input. Please try again (1-11).")
        start()


def length(user_input):
    print("""
1. Millimeters
2. Centimeters
3. Meters
4. Kilometers
5. Inches
6. Feet
7. Yards
8. Miles
9. Back""")
    
    
    choice = input("Please enter your choice: ")
    if choice == "1":
        print (f"your value in millimeters is: {user_input*1000}")
    elif choice == "2":
        print (f"your value in centimeters is: {user_input*100}")
    elif choice == "3":
        print (f"your value in meters is: {user_input}")
    elif choice == "4":
        print (f"your value in kilometers is: {user_input/1000}")
    elif choice == "5":
        print (f"your value in inches is: {user_input*39.3700787}")
    elif choice == "6":
        print (f"your value in feet is: {user_input*3.2808399}")
    elif choice == "7":
        print (f"your value in yards is: {user_input*1.0936133}")
    elif choice == "8":
        print (f"your value in miles is: {user_input*0.000621371192}")
    elif choice == "9":
        start()
    else:
        print("Invalid choice. Please try again.")
        length(user_input)
       
def volume(user_input):
    print("""
1. Milliliters
2. Centiliters
3. Deciliters
4. Liters
5. Cubic Meters
6. Cubic Inches
7. Cubic Feet
8. Cubic Yards
9.gallons
10. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Milliliters is: {user_input*1000}")
    elif choice == "2":
        print(f"your value in Centiliters is : {user_input*100}")
    elif choice == "3":
        print(f"your value in Deciliters is : {user_input*10}")
    elif choice == "4":
        print(f"your value in Litersis is : {user_input}")
    elif choice == "5":
        print(f"your value in Cubic Meters is : {user_input/1000}")
    elif choice == "6":
        print(f"your value in Cubic Inches is : {user_input*61.0237441}")
    elif choice == "7":
        print(f"your value in Cubic Feet is : {user_input*0.0353146667}")
    elif choice == "8":
        print(f"your value in Cubic Yards is : {user_input*0.00130795062}")
    elif choice == "9":
        print(f"your value in gallons is : {user_input*0.264172052}")
    elif choice == "10":
        start()
    else:
        print("Invalid choice. Please try again.")
        volume(user_input)
      
def weight(user_input):
    print("""
1. Milligrams
2. Grams
3. Kilograms
4. Ounces
5. Pounds
6. Back
        """)
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Milligrams is: {user_input*1000}")
    elif choice == "2":
        print(f"your value in Grams is : {user_input}")
    elif choice == "3":
        print(f"your value in Kilograms is : {user_input/1000}")
    elif choice == "4":
        print(f"your value in Ounces is : {user_input*35.2739619}")
    elif choice == "5":
        print(f"your value in Pounds is : {user_input*0.00220462262}")
    elif choice == "6":
        start()
    else:
        print("Invalid choice. Please try again.")
        weight(user_input)
    
def temperature(user_input):
    print("""
1. Celsius
2. Fahrenheit
3. Kelvin
4. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Celsius is: {user_input}")
    elif choice == "2":
        print(f"your value in Fahrenheit is : {user_input*1.8+32}")
    elif choice == "3":
        print(f"your value in Kelvin is : {user_input+273.15}")
    elif choice == "4":
        start()
    else:
        print("Invalid choice. Please try again.")
        temperature(user_input)

def area(user_input):
    print("""
1. Square Millimeters
2. Square Centimeters
3. Square Meters
4. Square Kilometers
5. Square Inches
6. Square Feet
7. Square Yards
8. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Square Millimeters is: {user_input*1000000}")
    elif choice == "2":
        print(f"your value in Square Centimeters is : {user_input*10000}")
    elif choice == "3":
        print(f"your value in Square Meters is : {user_input}")
    elif choice == "4":
        print(f"your value in Square Kilometers is : {user_input/1000000}")
    elif choice == "5":
        print(f"your value in Square Inches is : {user_input*1550.0031}")
    elif choice == "6":
        print(f"your value in Square Feet is : {user_input*10.7639104}")
    elif choice == "7":
        print(f"your value in Square Yards is : {user_input*1.19599005}")
    elif choice == "8":
        start()
    else:
        print("Invalid choice. Please try again.")
        area(user_input)
        
def speed(user_input):
    print("""
1. Meters per second
2. Kilometers per hour
3. Miles per hour
4. Meters per hour
5. Kilometers per second
6. Miles per second
7. Feet per second
8. Feet per minute
9. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Meters per second is: {user_input}")
    elif choice == "2":
        print(f"your value in Kilometers per hour is : {user_input*3.6}")
    elif choice == "3":
        print(f"your value in Miles per hour is : {user_input*2.23693629}")
    elif choice == "4":
        print(f"your value in Meters per hour is : {user_input*3600}")
    elif choice == "5":
        print(f"your value in Kilometers per second is : {user_input/1000}")
    elif choice == "6":
        print(f"your value in Miles per second is : {user_input*0.000621371192}")
    elif choice == "7":
        print(f"your value in Feet per second is : {user_input*3.2808399}")
    elif choice == "8":
        print(f"your value in Feet per minute is : {user_input*196.850394}")
    elif choice == "9":
        start()
    else:
        print("Invalid choice. Please try again.")
        speed(user_input)
        
def time(user_input):
    print("""
1. Milliseconds
2. Seconds
3. Minutes
4. Hours
5. Days
6. Weeks
7. Years
8. Decades
9. Centuries
10. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Milliseconds is: {user_input*1000}")
    elif choice == "2":
        print(f"your value in Seconds is : {user_input}")
    elif choice == "3":
        print(f"your value in Minutes is : {user_input/60}")
    elif choice == "4":
        print(f"your value in Hours is : {user_input/3600}")
    elif choice == "5":
        print(f"your value in Days is : {user_input/86400}")
    elif choice == "6":
        print(f"your value in Weeks is : {user_input/604800}")
    elif choice == "7":
        print(f"your value in Years is : {user_input/31536000}")
    elif choice == "8":
        print(f"your value in Decades is : {user_input/315360000}")
    elif choice == "9":
        print(f"your value in Centuries is : {user_input/3153600000}")
    elif choice == "10":
        start()
    else:
        print("Invalid choice. Please try again.")
        time(user_input)

def pressure(user_input):
    print("""
1. Pascals
2. Kilopascals
3. Megapascals
4. Bars
5. Atmospheres
6. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Pascals is: {user_input}")
    elif choice == "2":
        print(f"your value in Kilopascals is : {user_input/1000}")
    elif choice == "3":
        print(f"your value in Megapascals is : {user_input/1000000}")
    elif choice == "4":
        print(f"your value in Bars is : {user_input/100000}")
    elif choice == "5":
        print(f"your value in Atmospheres is : {user_input/101325}")
    elif choice == "6":
        start()
    else:
        print("Invalid choice. Please try again.")
        pressure(user_input)

def power(user_input):
    print("""
1. Watts
2. Kilowatts
3. Megawatts
4. Horsepower
5. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Watts is: {user_input}")
    elif choice == "2":
        print(f"your value in Kilowatts is : {user_input/1000}")
    elif choice == "3":
        print(f"your value in Megawatts is : {user_input/1000000}")
    elif choice == "4":
        print(f"your value in Horsepower is : {user_input/745.7}")
    elif choice == "5":
        start()
    else:
        print("Invalid choice. Please try again.")
        power(user_input)

def energy(user_input):
    print("""
1. Joules
2. Kilojoules
3. Calories
4. Kilocalories
5. Back
""")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print(f"your value in Joules is: {user_input}")
    elif choice == "2":
        print(f"your value in Kilojoules is : {user_input/1000}")
    elif choice == "3":
        print(f"your value in Calories is : {user_input/4.184}")
    elif choice == "4":
        print(f"your value in Kilocalories is : {user_input/4184}")
    elif choice == "5":
        start()
    else:
        print("Invalid choice. Please try again.")
        energy(user_input)
        
start()