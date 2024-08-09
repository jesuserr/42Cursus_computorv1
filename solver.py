from utils import strip, decimal_to_fraction

# Color codes for printings
BLUE = '\033[94m'
DEF = '\033[0m'

def print_reduced_form(coefficients):
    grade = 0
    print(f"{BLUE}Reduced form: {DEF}", end="")
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
    print(f"{BLUE}Polynomial degree: {DEF}" + str((len(coefficients) - 1)))

def print_complex_solution(numerator, denominator, discriminant, b, sign):
    print(f"{strip(numerator / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(-b / denominator), end="")
    print(f" {sign}" + " (√" + f"{strip(discriminant)}" + " / ", end="")
    print(f"{strip(denominator)}" + ")")

def print_results(discriminant, numerator1, numerator2, denominator, b):
    print(f"{BLUE}", end="")
    if discriminant > 0:
        print(f"Discriminant is strictly positive, the two solutions are:{DEF}")
    elif discriminant == 0:
        print(f"Discriminant is zero, the two solutions are identical:{DEF}")
    else:
        print(f"Discriminant is strictly negative, ", end="")
        print(f"the two complex solutions are:{DEF}")
        print_complex_solution(numerator1, denominator, discriminant, b, sign="-")
        print_complex_solution(numerator2, denominator, discriminant, b, sign="+")
        return
    print(f"{strip(numerator1 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(numerator1 / denominator))
    print(f"{strip(numerator2 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(numerator2 / denominator))

def solver(coefficients, max_degree):
    coefficients = coefficients[:]
    a, b, c = coefficients[2], coefficients[1], coefficients[0]
    if (len(coefficients) > 3):
        print_reduced_form(coefficients)
        raise ValueError("The polynomial degree is strictly greater than 2" +
        ", I can't solve.")
    if (a == 0 and b == 0 and c != 0):
        raise ValueError(f"Inconsistent equation." + "\n" + "No possible solutions.")
    if (a == 0 and b == 0 and c == 0):
        raise ValueError(f"{BLUE}Polynomial degree: {DEF}" + str(max_degree) +
        "\nInfinite solutions (each real number is a solution).")
    if a != 0:
        discriminant = (b ** 2) - (4 * a * c)
        numerator1 = -b - (discriminant) ** 0.5
        numerator2 = -b + (discriminant) ** 0.5
        denominator = 2 * a
        print_reduced_form(coefficients)
        print_results(discriminant, numerator1, numerator2, denominator, b)
        print_intermediate_steps(a, b, c, type="quadratic")
    else:
        coefficients.pop()
        print_reduced_form(coefficients)
        print(f"{BLUE}The solution is:{DEF}")
        print(f"{strip(c / -b, 30)}" + "->\t" + decimal_to_fraction(c / -b))
        print_intermediate_steps(a, b, c, type="linear")

def print_intermediate_steps(a, b, c, type):
    print(f"{BLUE}Intermediate steps:{DEF}")
    if type == "linear":
        print(f"Linear formula".ljust(30) + "->\t" + f"x = -b / a")
        print(f"Linear equation".ljust(30) + "->\t" + f"{b}x + {c} = 0")
        print(f"Coefficients".ljust(30) + "->\t" + "a =", b, ", b =", c)
        print(f"Solution".ljust(30) + "->\t" + f"x = -({c}) / {b} = ", end="")
        print(f"{strip(c / -b)}")
        return
    discriminant = (b ** 2) - (4 * a * c)
    numerator1 = -b - (discriminant) ** 0.5
    numerator2 = -b + (discriminant) ** 0.5
    print(f"Quadratic formula".ljust(30) + "->\t" + f"x = (-b ± √(b² - 4ac)) / 2a")
    print(f"Quadratic equation".ljust(30) + "->\t" + f"{a}x² + {b}x + {c} = 0")
    print(f"Coefficients".ljust(30) + "->\t" + "a =", a, ", b =", b, ", c =", c)
    print(f"Discriminant (Δ = b² - 4ac)".ljust(30) + "->\t", end="")
    print(f"Δ = {b}² - 4 * {a} * {c} =", f"{b ** 2} - ({4 * a * c}) =", end="")
    print(f" {discriminant}")
    print(f"First solution".ljust(30) + "->\t" + f"x1 = (-({b}) - ", end="")
    print(f"√{discriminant}) / {2 * a} =", f"{strip(numerator1 / (2 * a))}")
    print(f"Second solution".ljust(30) + "->\t" + f"x2 = (-({b}) + ", end="")
    print(f"√{discriminant}) / {2 * a} =", f"{strip(numerator2 / (2 * a))}")