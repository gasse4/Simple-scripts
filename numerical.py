from sympy import symbols, Eq, solve, sympify
import math
#definition symbols
a, b = symbols("a b")

# entering the count of symbols
count = int(input("Enter the count of (X and Y)'s elements: "))

# entering elements
X, Y = [], []
for i in range(count):
    num_x = float(input(f"Enter the element {i+1} of X: "))
    X.append(num_x)

for i in range(count):
    num_y = float(input(f"Enter the element {i+1} of Y: "))
    Y.append(num_y)

# calculate sums
sum_x = sum(X)
sum_y = sum(Y)
sum_x_squared = sum(x**2 for x in X)
sum_xy = sum(X[i] * Y[i] for i in range(count))
N = count

# # show sums
print(f"Sum of X: {sum_x}")
print(f"Sum of Y: {sum_y}")
print(f"Sum of X^2: {sum_x_squared}")
print(f"Sum of XY: {sum_xy}")
print(f"N (Number of elements): {N}")

# input the equations from the user
equation1 = input("Enter the first equation (e.g., 'sum_y = a*sum_x + b*N'): ")
equation2 = input("Enter the second equation (e.g., 'sum_xy = a*sum_x_squared + b*sum_x'): ")

# a dict to link the names with values
substitutions = {
    'sum_x': sum_x,
    'sum_y': sum_y,
    'sum_x_squared': sum_x_squared,
    'sum_xy': sum_xy,
    'N': N
}

try:
    # replacing the names with values
    eq1_lhs = sympify(equation1.split('=')[0], locals=substitutions)
    eq1_rhs = sympify(equation1.split('=')[1], locals=substitutions)
    eq2_lhs = sympify(equation2.split('=')[0], locals=substitutions)
    eq2_rhs = sympify(equation2.split('=')[1], locals=substitutions)

    # creation two equations
    eq1 = Eq(eq1_lhs, eq1_rhs)
    eq2 = Eq(eq2_lhs, eq2_rhs)

    # solve two equations
    solution = solve((eq1, eq2), (a, b))

    # show the result
    print(f"Solution:\na = {solution[a]:.4f}\nb = {solution[b]:.4f}")
except Exception as e:
    print(f"An error occurred while processing the equations: {e}")
    
print("The best fitting is : ")
print(f"y = {solution[a]:.4f}*x + {solution[b]:.4f}")

y_x = [(solution[a] * x + solution[b]) for x in X]

RMSE = math.sqrt(sum((y_actual - y_predicted) ** 2 for y_actual, y_predicted in zip(Y, y_x)) / N)
print(f"RMSE : {RMSE:.4f}")
