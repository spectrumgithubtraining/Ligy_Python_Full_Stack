import cmath  # Using cmath to handle complex numbers

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two solutions
    solution1 = (-b + discriminant) / (2*a)
    solution2 = (-b - discriminant) / (2*a)

    return solution1, solution2

# Input coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Solve the quadratic equation
solutions = solve_quadratic(a, b, c)

# Display the solutions
print("Solutions:", solutions)
