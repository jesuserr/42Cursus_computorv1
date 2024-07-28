
############################### CONSTANTS & INITS ##############################


#################################### CLASSES ###################################


################################### FUNCTIONS ##################################
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def decimalToFraction(number):
    integer_part = int(number)
    fractional_part = number - integer_part
    precision = 1000000000
    gcd_value = gcd(round(fractional_part * precision), precision)
    numerator = round(fractional_part * precision) // gcd_value
    denominator = precision // gcd_value
    return (f"Irreductible fraction: {(integer_part * denominator) + numerator} / {denominator}")

def print_results(discriminant, numerator1, numerator2, denominator):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(f"{numerator1 / denominator:.9f}\t->\t" + decimalToFraction(numerator1 / denominator))
        print(f"{numerator2 / denominator:.9f}\t->\t" + decimalToFraction(numerator2 / denominator))
    elif discriminant < 0:
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(f"{numerator1 / denominator:.9f}")
        print(f"{numerator2 / denominator:.9f}")
    else:
        print("Discriminant is zero, the two solutions are identical:")
        print(f"{numerator1 / denominator:.9f}\t->\t" + decimalToFraction(numerator1 / denominator))
    
def solver():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    c = float(input("Enter a third number: "))
    discriminant = (b ** 2) - (4 * a *c)
    numerator1 = -b - (discriminant) ** 0.5
    numerator2 = -b + (discriminant) ** 0.5
    denominator = 2 * a
    print_results(discriminant, numerator1, numerator2, denominator)

################################# MAIN FUNCTION ################################

if __name__ == '__main__':
    solver()    

# python3 computor.py "2x^2-5x+3=0"     -> two solutions
# python3 computor.py "x^2-4x+4=0"      -> two identical solutions
# python3 computor.py "x^2-10x+25=0"    -> two identical solutions
# python3 computor.py "x^2-4x+5=0"      -> complex
# python3 computor.py "x^2-x+1=0"       -> complex
# python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# 3x^2-10x+7=0 (7/3 , 1) no funciona la fraccion
# 3x^2-2x=0 (0, 2/3) no funciona la fraccion

# TODOs:
# irreductible fraction for complex numbers