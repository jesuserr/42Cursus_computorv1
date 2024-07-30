import sys

################################### FUNCTIONS ##################################

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
    return (f"Irreducible fraction: {(integer_part * denominator) + numerator} / {denominator}")

def print_reduced_form(coefficients):
    grade = 0
    print("Reduced form: ", end="")
    for coefficient in coefficients:
        if coefficient > 0:
            if grade != 0:
                print(f"+ ", end="")
            print(f"{coefficient}".rstrip('0').rstrip('.') + f" * X^{grade} ", end="")
        elif coefficient < 0:
            print(f"- ", end="")
            print(f"{abs(coefficient)}".rstrip('0').rstrip('.') + f" * X^{grade} ", end="")
        else:
            if grade != 0:
                print(f"+ ", end="")
            print(f"0" + f" * X^{grade} ", end="")
        if (grade == len(coefficients) - 1):
            print("= 0")
            break
        grade += 1
    print(f"Polynomial degree: " + str((len(coefficients) - 1)))

def print_results(discriminant, numerator1, numerator2, denominator, b):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
    elif discriminant == 0:
        print("Discriminant is zero, the two solutions are identical:")
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(f"{numerator1 / denominator:.9f}".ljust(30) + "->\t" + f"{decimal_to_fraction(-b / denominator)}".rstrip('0').rstrip('.') + " - (√" + f"{discriminant:.9f}".rstrip('0').rstrip('.') + " / " f"{denominator:.9f}".rstrip('0').rstrip('.') + ")")
        print(f"{numerator2 / denominator:.9f}".ljust(30) + "->\t" + f"{decimal_to_fraction(-b / denominator)}".rstrip('0').rstrip('.') + " + (√" + f"{discriminant:.9f}".rstrip('0').rstrip('.') + " / " f"{denominator:.9f}".rstrip('0').rstrip('.') + ")")
        return
    print(f"{numerator1 / denominator:.9f}".rstrip('0').rstrip('.').ljust(20) + "->\t" + decimal_to_fraction(numerator1 / denominator))
    print(f"{numerator2 / denominator:.9f}".rstrip('0').rstrip('.').ljust(20) + "->\t" + decimal_to_fraction(numerator2 / denominator))

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
        print(f"{c / -b:.9f}".rstrip('0').rstrip('.').ljust(20) + "->\t" + decimal_to_fraction(c / -b))

def parser(arguments):
    coefficients = []
    for argument in arguments.split(" "):
        coefficients.append(float(argument))
    return coefficients

################################# MAIN FUNCTION ################################

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: python3 computor.py \"equation\"")
        exit(1)
    coefficients = parser(sys.argv[1])
    if (len(coefficients) <= 3):
        solver(coefficients[2], coefficients[1], coefficients[0])
    else:
        print_reduced_form(coefficients)
        print("The polynomial degree is strictly greater than 2, I can't solve.")

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

# TODOs:
# improve decimal_to_fraction
# irreducible fraction for complex numbers (DONE)