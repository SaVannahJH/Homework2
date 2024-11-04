# SaVannah Hussey
# UWYO COSC 1010
# 11/4/2024
# Lab 08
# Lab Section:14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_string(s):
    if s.isdigit():
        return int(s)
    
    try:
        float_value = float(s)
        
        if '.' in s:
            parts = s.split('.')
            if len(parts) > 2 or len(parts[1]) == 0:
                return False
            
        return float_value
    except ValueError:
        return False

print(convert_string("150"))     
print(convert_string("55.61"))    
print(convert_string("45.67.89")) 
print(convert_string("abcde"))       
print(convert_string("12."))       
print(convert_string("3.1400"))      


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_bound, upper_bound):
    if not (isinstance(lower_bound, int) and isinstance(upper_bound, int)):
        return False
    if lower_bound > upper_bound:
        return False
    
    y_values = []
    for x in range(lower_bound, upper_bound + 1):
        y = m * x + b
        y_values.append(y)
    
    return y_values

def main():
    while True:
        user_input = input("Enter m, b, lower x bound, upper x bound (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            m, b, lower_x, upper_x = user_input.split()
            m = float(m)  
            b = float(b)  
            lower_x = int(lower_x)  
            upper_x = int(upper_x)  
            
            result = slope_intercept(m, b, lower_x, upper_x)
            print(result)
        except ValueError:
            print("Invalid input. Please ensure you enter numbers for m, b, lower x, and upper x bounds.")

if __name__ == "__main__":
    main()

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def square_root(x):
    """Calculate the square root of x using the Babylonian method. Return None if x is negative."""
    if x < 0:
        return None
    guess = x / 2.0
    while True:
        new_guess = (guess + x / guess) / 2
        if abs(new_guess - guess) < 1e-10: 
            break
        guess = new_guess
    return guess

def solve_quadratic(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0."""
    discriminant = b ** 2 - 4 * a * c
    sqrt_discriminant = square_root(discriminant)
    
    if sqrt_discriminant is None:
        return None  
    
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    return root1, root2

def main():
    while True:
        user_input = input("Enter a, b, c (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            a, b, c = map(float, user_input.split())
            
            roots = solve_quadratic(a, b, c)
            if roots is None:
                print("The equation has no real roots.")
            else:
                print(f"The roots are: {roots[0]} and {roots[1]}")
        except ValueError:
            print("Invalid input. Please ensure you enter numbers for a, b, and c.")

if __name__ == "__main__":
    main()
