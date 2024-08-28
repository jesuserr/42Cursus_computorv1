from utils import strip, decimal_to_fraction

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

def print_irreducible_complex(numerator, denominator, discriminant, b, sign):
    if sign == "-":
        print(f"{BLUE}Irreducible fractions: {DEF}")
    print(f"{strip(numerator / denominator, 30)}" + "->\t(", end="")
    print(decimal_to_fraction(-b / denominator), end="")
    print(f") {sign}" + " (√" + f"{strip(discriminant)}" + " / ", end="")
    print(f"{strip(denominator)}" + ")")

def print_irreducible_fractions(numerator1, numerator2, denominator):
    if numerator1 == numerator2:
        print(f"{BLUE}Irreducible fraction: {DEF}")
        print(f"{strip(numerator1 / denominator, 30)}" + "->\t", end="")
        print(decimal_to_fraction(numerator1 / denominator))                                  
        return
    print(f"{BLUE}Irreducible fractions: {DEF}")
    print(f"{strip(numerator1 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(numerator1 / denominator))
    print(f"{strip(numerator2 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(numerator2 / denominator))

def print_results(a, b, c, irreducible):
    discriminant = (b ** 2) - (4 * a * c)
    numerator1 = -b - (discriminant) ** 0.5
    numerator2 = -b + (discriminant) ** 0.5
    denominator = 2 * a
    print(f"{BLUE}", end="")
    if discriminant > 0:
        print(f"Discriminant is strictly positive, the two solutions are:{DEF}")
    elif discriminant == 0:
        print(f"Discriminant is zero, the two solutions are identical:{DEF}")
    else:
        print(f"Discriminant is strictly negative, ", end="")
        print(f"the two complex solutions are:{DEF}")
    print(f"{strip(numerator1 / denominator, 30)}")
    print(f"{strip(numerator2 / denominator, 30)}")
    if irreducible and discriminant >= 0:
        print_irreducible_fractions(numerator1, numerator2, denominator)
    elif irreducible and discriminant < 0:        
        print_irreducible_complex(numerator1, denominator, discriminant, b, "-")
        print_irreducible_complex(numerator2, denominator, discriminant, b, "+")

def solver(coefficients, steps, irreducible):
    # Creates copy of coefficients list since is modified when a = 0
    coefficients = coefficients[:]
    a, b, c = coefficients[2], coefficients[1], coefficients[0]
    if (len(coefficients) > 3 and not all(coef == 0 for coef in coefficients[3:])):
        print_reduced_form(coefficients)
        raise ValueError("The polynomial degree is strictly greater than 2" +
        ", I can't solve.")
    if (a == 0 and b == 0 and c != 0):
        raise ValueError(f"Inconsistent equation." + "\n" + "No possible solutions.")
    if all(coef == 0 for coef in coefficients):
        raise ValueError(f"{BLUE}Polynomial degree: {DEF}" + "Not Applicable" +
        "\nInfinite solutions (each real number is a solution).")
    if a != 0:
        print_reduced_form(coefficients)
        print_results(a, b, c, irreducible)
        print_intermediate_steps(a, b, c, type="quadratic") if steps else None
    else:
        coefficients.pop()
        print_reduced_form(coefficients)
        print(f"{BLUE}The solution is:{DEF}\n" + f"{strip(c / -b, 30)}")
        print_irreducible_fractions(c, c, -b) if irreducible else None
        print_intermediate_steps(a, b, c, type="linear") if steps else None

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