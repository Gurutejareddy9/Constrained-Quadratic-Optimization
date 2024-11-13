import numpy as np
from scipy.optimize import minimize

# Define the quadratic objective function
def objective(x):
    return x[0]**2 + x[1]**2  # f(x) = x1^2 + x2^2

# Define the constraints
def constraint1(x):
    return x[0] + x[1] - 1  # x1 + x2 >= 1

def constraint2(x):
    return x[0]  # x1 >= 0

def constraint3(x):
    return x[1]  # x2 >= 0

# Initial guess
x0 = [0.5, 0.5]

# Constraints dictionary
constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2},
    {'type': 'ineq', 'fun': constraint3}
]

# Solve the optimization problem
result = minimize(objective, x0, constraints=constraints, method='SLSQP')

# Display the results
print("Optimal Solution:", result.x)
print("Objective Value at Optimal Solution:", result.fun)
print("Success:", result.success)
print("Message:", result.message)
