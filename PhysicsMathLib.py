'''
Independant physocs library fro Matt B
from  chatGPT? or some AI bot
November, 2024
'''

import math

def solve_linear_equation(equation):
    '''
    Linear Equation
    '''
    equation = equation.replace(" ", "")
    left_side, right_side = equation.split("=")
    if "X" in left_side:
        left_side = left_side.replace("X", "")
        if left_side == "":
            left_side = "0"
        constant = float(left_side)
    else:
        constant = 0
    right_side = float(right_side)
    X = right_side + constant
    return X

def solve_quadratic(a, b, c):
    '''
    Quadratic Solver
    '''
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return None

def gcd(a, b):
    '''
    modulo return
    '''
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    '''
    Simplify fractions
    '''
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def solve_fraction(expression):
    '''
    def
    '''
    try:
        evaluated_result = eval(expression)
        numerator, denominator = evaluated_result.as_integer_ratio()
        simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
        decimal_result = evaluated_result
        return (simplified_numerator, simplified_denominator), decimal_result
    except ZeroDivisionError:
        return "Error: Division by zero", None
    except Exception as e:
        return f"Error: {e}", None

def mean(data):
    '''
    def
    '''
    return sum(data) / len(data)

def median(data):
    '''
    def
    '''
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

def stdev(data):
    '''
    def
    '''
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)

def descriptive_statistics(data):
    '''
    def
    '''
    try:
        data = list(map(float, data.split(',')))
        mean_value = mean(data)
        median_value = median(data)
        stdev_value = stdev(data)
        return mean_value, median_value, stdev_value
    except Exception as e:
        return f"Error: {e}"

def probability(event_outcomes, total_outcomes):
    '''
    def
    '''
    try:
        event_outcomes = float(event_outcomes)
        total_outcomes = float(total_outcomes)
        prob = event_outcomes / total_outcomes
        return prob
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {e}"

def plot_data(x_values, y_values):
    '''
    def
    '''
    plt = ti_plotlib()
    plt.cls()
    plt.grid(1, 1, "dotted")
    plt.plot(x_values, y_values, "b-")
    plt.show_plot()

def ai_guide():
    '''
    def
    '''
    print("Hello! I'm your AI guide. How can I assist you today?")
    print("1. Basic Arithmetic (e.g., 2 + 3 * 4)")
    print("2. Solve Linear Equation (e.g., X - 5 = 4)")
    print("3. Solve Quadratic Equation (e.g., 2X^2 + 3X + 1 = 0)")
    print("4. Solve Fraction Problem (e.g., 1/2 + 3/4)")
    print("5. Descriptive Statistics (e.g., 1,2,3,4,5)")
    print("6. Probability Calculation (e.g., event outcomes: 3, total outcomes: 10)")
    print("7. Plot Data (e.g., x-values: 1,2,3, y-values: 4,5,6)")
   
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
   
    if choice == "1":
        expression = input("Enter the arithmetic expression (e.g., 2 + 3 * 4): ")
        try:
            result = eval(expression)
            print(f"The result is {result}")
        except Exception as e:
            print(f"Error: {e}")
    elif choice == "2":
        equation = input("Enter the linear equation (e.g., X - 5 = 4): ")
        solution = solve_linear_equation(equation)
        print(f"The solution is X = {solution}")
    elif choice == "3":
        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            roots = solve_quadratic(a, b, c)
            if roots:
                if len(roots) == 2:
                    print(f"The roots are {roots} and {roots}")
                else:
                    print(f"The root is {roots}")
            else:
                print("No real roots")
        except Exception as e:
            print(f"Error: {e}")
    elif choice == "4":
        expression = input("Enter the fraction expression (e.g., 1/2 + 3/4): ")
        fraction_result, decimal_result = solve_fraction(expression)
        if decimal_result is not None:
            print(f"The result is {fraction_result}/{fraction_result} (fraction) or {decimal_result} (decimal)")
        else:
            print(fraction_result)
    elif choice == "5":
        data = input("Enter the data set (comma-separated values, e.g., 1,2,3,4,5): ")
        stats = descriptive_statistics(data)
        if isinstance(stats, tuple):
            mean_value, median_value, stdev_value = stats
            print(f"Mean: {mean_value}, Median: {median_value}, Standard Deviation: {stdev_value}")
        else:
            print(stats)
    elif choice == "6":
        event_outcomes = input("Enter the number of event outcomes: ")
        total_outcomes = input("Enter the total number of outcomes: ")
        prob = probability(event_outcomes, total_outcomes)
        print(f"The probability is {prob}")
    elif choice == "7":
        x_values = list(map(float, input("Enter the x-values (comma-separated): ").split(',')))
        y_values = list(map(float, input("Enter the y-values (comma-separated): ").split(',')))
        plot_data(x_values, y_values)
    else:
        print("Invalid choice. Please run the program again.")

def main():
    '''
    main
    '''
    ai_guide()

main()