# Title: Numeric Integration of Two Curves Area - Python Implementation
# Purpose: To find the area between two curves

# Library Imports
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from sympy import symbols, sympify

# Function Definitions
## Get input from user and return a function
def getInput(var):
    if var == 0: return 0
    try:
        func = lambda x: eval(var.replace('^', '**'))
        return func
    except (SyntaxError, NameError):
        print("Invalid function syntax. Please try again.")

## Evaluate an expression with a given value for x
def evaluate_expression(expression, x_value):
    x = symbols('x')
    try:
        res = sympify(expression).subs(x, x_value)
        return float(res) if res.is_real else np.nan
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return np.nan

## Find the area between two curves
def findArea(f, L, U):
    area = round(abs(quad(lambda x: f(x), min(L), max(U))[0]), 5)
    print(f"Area between curves: {area}")
    return area

## Plot the two curves and the area between them
def plot_equations(h, f, g, limL, limU, L, U):
    x  = symbols('x')
    Lx = np.linspace(limL-5, max(L), 100)
    Ux = np.linspace(min(U), limU+5, 100)
    xVal  = np.linspace(limL - 5, limU + 5, 100)
    yVal1 = [evaluate_expression(f, x) for x in xVal]
    yVal2 = [evaluate_expression(g, x) for x in xVal]

    area = findArea(h, L, U)

    if min(yVal1) <= min(yVal2): min_y = min(yVal1)
    else: min_y = min(yVal2)
    if max(yVal1) >= max(yVal2): max_y = max(yVal1)
    else: max_y = max(yVal2)

    plt.plot(xVal, yVal1, label=f'f(x) = {f.replace("**", "^").replace("*", "").replace("  ", " ")}')
    plt.plot(xVal, yVal2, label=f'g(x) = {g.replace("**", "^").replace("*", "").replace("  ", " ")}')

    plt.fill_between(xVal, yVal1, yVal2, color='gray', alpha=0.3, label='Area between curves')
    plt.fill_between(Lx, min_y, max_y, color='white')
    plt.fill_between(Ux, min_y, max_y, color='white')

    plt.axvline(min(L), color='black', linestyle='--', label='limits')
    plt.axvline(max(U), color='black', linestyle='--')

    plt.annotate(f'Area between curves: {area}', xy=(0, 1.03), xycoords='axes fraction')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid()
    plt.show()

# Main Function
equat1 = input("Input first equation  : ")
equat2 = input("Input second equation : ")
Llimit = float(input("Input lower limit     : "))
Ulimit = float(input("Input upper limit     : "))

equals = lambda x: getInput(equat1)(x) - getInput(equat2)(x)
L = [Llimit]
U = [Ulimit]

if Llimit >= 5: Llimit = 5
if Ulimit <= -5: Ulimit = -5

plot_equations(equals, equat1, equat2, Llimit, Ulimit, L, U)
