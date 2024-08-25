def print_irreducible_complex(numerator1, numerator2, denominator, discriminant, b):    
    print(f"{strip(numerator1 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(-b / denominator), end="")
    print(f" -" + " (√" + f"{strip(discriminant)}" + " / ", end="")
    print(f"{strip(denominator)}" + ")")
    print(f"{strip(numerator2 / denominator, 30)}" + "->\t", end="")
    print(decimal_to_fraction(-b / denominator), end="")
    print(f" +" + " (√" + f"{strip(discriminant)}" + " / ", end="")
    print(f"{strip(denominator)}" + ")")



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
        if irreducible:
            print(f"{BLUE}Irreducible fractions: {DEF}")
            print_irreducible_complex(numerator1, denominator, discriminant, b, "-")
            print_irreducible_complex(numerator2, denominator, discriminant, b, "+")
        return
    print(f"{strip(numerator1 / denominator, 30)}")
    print(f"{strip(numerator2 / denominator, 30)}")
    if irreducible:
        print_irreducible_fractions(numerator1, numerator2, denominator)