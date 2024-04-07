def fixed_point_iteration(x0, num_iterations):
    """
    Performs fixed-point iteration for the given number of iterations.
    """
    x = x0
    for i in range(num_iterations):
        x = (0.5 - x) / 3 + x
    return x

# Initial guess for x0
x0 = 1/6

# Number of iterations
num_iterations = 10000000

# Perform fixed-point iteration
result = fixed_point_iteration(x0, num_iterations)

print("Result after", num_iterations, "iterations:", result)
