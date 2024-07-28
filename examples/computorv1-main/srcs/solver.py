import re
import math, cmath

def _sqrt(number, isnegative, guess=0.0,):
    if guess == 0.0:
        guess = number / 2.0
    better_guess = (guess + number / guess) / 2.0
    if abs(guess - better_guess) < 0.000001:
        if isnegative:
            return better_guess * 1j
        return better_guess
    else:
        return _sqrt(number, isnegative, better_guess)

def print_reduced_form(a, b, c):
    print("Reduced form: ", end="")
    if a != 0:
        print(a, end="")
        print(" * X^2 ", end="")
    if b != 0:
        if a != 0:
            if b > 0:
                print("+ ", end="")
            else:
                print("- ", end="")
        print(abs(b), end="")
        print(" * X ", end="")
    if c != 0:
        if c > 0:
            print("+ ", end="")
        else:
            print("- ", end="")
        print(abs(c), end="")
    print(" = 0")

def solve_equation(a, b, c):
    # print_reduced_form(a, b, c)
    if a == 0:
        if b == 0:
            if c == 0:
                # print("Polinomial degree: 0")
                print("Infinite solutions")
                return None
            else:
                # print("Polinomial degree: 0")
                print("No solution")
                return None
        else:
            solution = -c / b
            # print("Polinomial degree: 1")
            print("Irreductible fraction: ", f"-{c} / {b}")
            print("The solution is:\n", solution)
            return solution
    else:  
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            # print("Polinomial degree: 2")
            root1 = (-b + _sqrt(-discriminant, True)) / (2*a)
            root2 = (-b - _sqrt(-discriminant, True)) / (2*a)
            root1 = str((root1.real)) + " + " + str(root1.imag) + "i"
            root1 = root1.replace("+ -", "- ")
            root2 = str((root2.real)) + " + " + str(root2.imag) + "i"
            root2 = root2.replace("+ -", "- ")
            print("Discriminant is strictly negative, the two complex solutions are:\n", f"-{b} + √{discriminant} / {(2*a)} = {root1}", "\n", f"-{b} - √{discriminant} / {(2*a)} = {root2}")
        elif discriminant == 0: 
            root = -b / (2*a)
            # print("Polinomial degree: 2")
            print("Irreductible fraction: ", f"-{b} / {(2*a)}")
            print("Discriminant is zero, the solution is:", root)
            return root
        else: 
            root1 = (-b + _sqrt(discriminant, False)) / (2*a)
            root2 = (-b - _sqrt(discriminant, False)) / (2*a)
            print("Polinomial degree: 2")
            print("Discriminant is strictly positive, the two solutions are:\n", f"-{b} + √{discriminant} / {(2*a)} = {root1}", "\n", f"-{b} - √{discriminant} / {(2*a)} = {root2}")