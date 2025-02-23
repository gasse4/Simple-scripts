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


yearly_salary = int(get_positive_float("Enter your yearly salary: "))
portion_saved = float(get_portion_saved("Enter the portion of salary: "))
cost_of_dream_house = float(get_positive_float("Enter the cost of your dream house: "))
semi_annual_raise = float(get_portion_saved("Enter the semi annual raise: "))

portion_down_payment = 0.25 * cost_of_dream_house
monthly_salary = yearly_salary / 12
annual_rate = 0.05
amount_saved = 0
months = 0
monthly_rate = annual_rate / 12

while amount_saved < portion_down_payment:
    amount_saved += monthly_salary * portion_saved
    amount_saved += amount_saved * monthly_rate
    months += 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

print(f"It will take {months} months to save for the down payment.")
