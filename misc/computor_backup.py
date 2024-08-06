import sys
import re
from itertools import chain

################################### CONSTANTS ##################################

DECIMAL_PRECISION = ".9f"

################################### FUNCTIONS ##################################

def strip(number, justify=0):
    if number == -0:
        number = 0
    return f"{number:{DECIMAL_PRECISION}}".rstrip('0').rstrip('.').ljust(justify)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def decimal_to_fraction(number):
    integer_part = int(number)
    fractional_part = number - integer_part
    precision = 1000000000
    gcd_value = gcd(round(fractional_part * precision), precision)
    numerator = round(fractional_part * precision) // gcd_value
    denominator = precision // gcd_value
    string = f"{(integer_part * denominator) + numerator} / {denominator}"
    return (f"Irreducible fraction: {string}")

def print_reduced_form(coefficients):
    grade = 0
    print("Reduced form: ", end="")
    for coefficient in coefficients:
        if coefficient > 0:
            if grade != 0:
                print(f"+ ", end="")
            print(f"{strip(coefficient)}"+ f" * X^{grade} ", end="")
        elif coefficient < 0:
            print(f"- ", end="")
            print(f"{strip(abs(coefficient))}" + f" * X^{grade} ", end="")
        else:
            if grade != 0:
                print(f"+ ", end="")
            print(f"0" + f" * X^{grade} ", end="")
        if (grade == len(coefficients) - 1):
            print("= 0")
            break
        grade += 1
    print(f"Polynomial degree: " + str((len(coefficients) - 1)))

def print_complex_solution(numerator, denominator, discriminant, b, sign):
    print(f"{strip(numerator / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(-b / denominator), end="")
    print(f" {sign}" + " (√" + f"{strip(discriminant)}" + " / ", end="")
    print(f"{strip(denominator)}" + ")")

def print_results(discriminant, numerator1, numerator2, denominator, b):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
    elif discriminant == 0:
        print("Discriminant is zero, the two solutions are identical:")
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        print_complex_solution(numerator1, denominator, discriminant, b, sign="-")
        print_complex_solution(numerator2, denominator, discriminant, b, sign="+")
        return
    print(f"{strip(numerator1 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(numerator1 / denominator))
    print(f"{strip(numerator2 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(numerator2 / denominator))

def solver(a, b, c):
    if a != 0:
        discriminant = (b ** 2) - (4 * a *c)
        numerator1 = -b - (discriminant) ** 0.5
        numerator2 = -b + (discriminant) ** 0.5
        denominator = 2 * a
        print_reduced_form(coefficients)
        print_results(discriminant, numerator1, numerator2, denominator, b)
    else:
        coefficients.pop()
        print_reduced_form(coefficients)
        print("The solution is:")
        print(f"{strip(c / -b, 30)}" + "->\t" + decimal_to_fraction(c / -b))

def pre_parser(arguments):
    allowed_chars = "0123456789*+-xX^=. "
    if not all(char in allowed_chars for char in arguments):
        raise ValueError("Invalid characters in input")
    arguments_no_blanks = arguments.replace(" ", "")
    invalid_sequences = ["**", "++", "--", "xx", "XX", "xX", "Xx" , "^^", "=="]
    invalid_sequences += ["..", "+-", "-+", "^-", "^+", "-*", "+*", "*-", "*+"]
    invalid_sequences += ["-^", "+^"]
    for seq in invalid_sequences:
        if seq in arguments_no_blanks:
            raise ValueError(f"Invalid sequence found: {seq}")
    identity_sides = arguments_no_blanks.split("=")
    if len(identity_sides) != 2:
        raise ValueError("Invalid number of equal signs")
    if identity_sides[0] == "" or identity_sides[1] == "":
        raise ValueError("Invalid number of expressions")
    return(identity_sides)

def find_max_degree(left_terms, right_terms):
    max_degree = 0
    for terms in chain(left_terms, right_terms):
        if re.search(r'[xX]\^\d+\.\d+', terms):
            raise ValueError("Invalid exponent, must be integer")
        match = re.findall(r'[xX]\^(\d+)', terms)
        if match:
            if int(match[0]) > max_degree:
                max_degree = int(match[0])
    return max_degree

def parser(arguments):
    identity_sides = pre_parser(arguments)
    left_terms = re.split(r'(?=[+-])', identity_sides[0])
    right_terms = re.split(r'(?=[+-])', identity_sides[1])
    left_terms = [term for term in left_terms if term]
    right_terms = [term for term in right_terms if term]
    coefficients = [0.0] * max(3, find_max_degree(left_terms, right_terms) + 1)
    for terms in left_terms:
        match = re.findall(r'([+-]?\d*\.?\d*)\*[xX]\^(\d+)', terms)
        if match:
            coefficients[int(match[0][1])] += float(match[0][0])
    for terms in right_terms:
        match = re.findall(r'([+-]?\d*\.?\d*)\*[xX]\^(\d+)', terms)
        if match:
            coefficients[int(match[0][1])] += -1 * float(match[0][0])
    print(identity_sides, left_terms, right_terms, len(left_terms), len(right_terms))
    print(find_max_degree(left_terms, right_terms))
    print(coefficients)
    return coefficients

################################# MAIN FUNCTION ################################

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: python3 computor.py \"equation\"")
        exit(1)
    try:
        coefficients = parser(sys.argv[1])
        if (coefficients[0] == 0 and coefficients[1] == 0 and coefficients[2] == 0):
            print("Reduced form: 0 * X^0 = 0")
            print(f"Polynomial degree: 0" + "\n" + "Infinite solutions")
        elif (len(coefficients) <= 3):
            solver(coefficients[2], coefficients[1], coefficients[0])
        else:
            print_reduced_form(coefficients)
            print("The polynomial degree is strictly greater than 2, I can't solve.")
    except ValueError as error:
        print(error)
        exit(1)

# "2x^2-5x+3=0"     -> two solutions
# python3 computor.py "3 -5 2"

# "x^2-4x+4=0"      -> two identical solutions
# python3 computor.py "4 -4 1"

# "x^2-10x+25=0"    -> two identical solutions
# python3 computor.py "25 -10 1"

# "x^2-4x+5=0"      -> complex
# python3 computor.py "5 -4 1"

# "x^2-x+1=0"       -> complex
# python3 computor.py "1 -1 1"

# python3 computor.py "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
# python3 computor.py "4 4 -9.3"

# 3x^2-10x+7=0 (7/3 , 1) no funciona la fraccion
# 3x^2-2x=0 (0, 2/3) no funciona la fraccion

# que no acepte numero sin x
# python3 computor.py "8 * X^0 = 8" -> error