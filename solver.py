DECIMAL_PRECISION = ".9f"

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

def solver(coefficients, max_degree):
    a, b, c = coefficients[2], coefficients[1], coefficients[0]
    if (a == 0 and b == 0 and c != 0):
        raise ValueError(f"Inconsistent equation." + "\n" + "No possible solutions.")
    if (a == 0 and b == 0 and c == 0 and max_degree == 0):
        raise ValueError(f"Polynomial degree: 0 \nIdentity equation.")
    if (a == 0 and b == 0 and c == 0 and max_degree > 0):
        raise ValueError(f"Polynomial degree: " + str(max_degree) +
        "\nInfinite solutions.")
    if (len(coefficients) > 3):
        print_reduced_form(coefficients)
        raise ValueError("The polynomial degree is strictly greater than 2" +
        ", I can't solve.")
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
