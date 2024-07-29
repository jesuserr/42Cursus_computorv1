import sys

############################### CONSTANTS & INITS ##############################
#################################### CLASSES ###################################
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
        if (grade == len(coefficients) - 1):
            print("= 0")
            break
        grade += 1
    print(f"Polynomial degree: " + str((len(coefficients) - 1)))

def print_results(discriminant, numerator1, numerator2, denominator):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
    elif discriminant == 0:
        print("Discriminant is zero, the two solutions are identical:")
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(f"{numerator1 / denominator:.9f}" + "\n" + f"{numerator2 / denominator:.9f}")
        return
    print(f"{numerator1 / denominator:.9f}".rstrip('0').rstrip('.').ljust(20) + "->\t" + decimal_to_fraction(numerator1 / denominator))
    print(f"{numerator2 / denominator:.9f}".rstrip('0').rstrip('.').ljust(20) + "->\t" + decimal_to_fraction(numerator2 / denominator))

def solver(arguments):
    coefficients = []
    c = float(arguments.split(" ")[0])
    coefficients.append(c)
    b = float(arguments.split(" ")[1])
    coefficients.append(b)
    a = float(arguments.split(" ")[2])
    coefficients.append(a)    
    discriminant = (b ** 2) - (4 * a *c)
    numerator1 = -b - (discriminant) ** 0.5
    numerator2 = -b + (discriminant) ** 0.5
    denominator = 2 * a
    print_reduced_form(coefficients)
    print_results(discriminant, numerator1, numerator2, denominator)

################################# MAIN FUNCTION ################################

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: python3 computor.py \"equation\"")
        exit(1)    
    solver(sys.argv[1])

# python3 computor.py "2x^2-5x+3=0"     -> two solutions
# python3 computor.py "2 -5 3"

# python3 computor.py "x^2-4x+4=0"      -> two identical solutions
# python3 computor.py "1 -4 4"

# python3 computor.py "x^2-10x+25=0"    -> two identical solutions
# python3 computor.py "1 -10 25"

# python3 computor.py "x^2-4x+5=0"      -> complex
# python3 computor.py "1 -4 5"

# python3 computor.py "x^2-x+1=0"       -> complex
# python3 computor.py "1 -1 1"

# python3 computor.py "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
# python3 computor.py "-9.3 4 4"

# 3x^2-10x+7=0 (7/3 , 1) no funciona la fraccion
# 3x^2-2x=0 (0, 2/3) no funciona la fraccion

# TODOs:
# irreducible fraction for complex numbers