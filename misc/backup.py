def print_results(discriminant, numerator1, numerator2, denominator):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(f"{numerator1 / denominator:.9f}".rstrip('0').rstrip('.') + "\t->\t" + decimalToFraction(numerator1 / denominator))
        print(f"{numerator2 / denominator:.9f}".rstrip('0').rstrip('.') + "\t->\t" + decimalToFraction(numerator2 / denominator))
    elif discriminant < 0:
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(f"{numerator1 / denominator:.9f}")
        print(f"{numerator2 / denominator:.9f}")
    else:
        print("Discriminant is zero, the two solutions are identical:")
        print(f"{numerator1 / denominator:.9f}".rstrip('0').rstrip('.') + "\t->\t" + decimalToFraction(numerator1 / denominator))
        print(f"{numerator2 / denominator:.9f}".rstrip('0').rstrip('.') + "\t->\t" + decimalToFraction(numerator2 / denominator))


def print_results(discriminant, numerator1, numerator2, denominator, b):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
    elif discriminant == 0:
        print("Discriminant is zero, the two solutions are identical:")
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(f"{numerator1 / denominator:.9f}" + "\n" + f"{numerator2 / denominator:.9f}")
        print(f"{numerator1 / denominator:.9f}".ljust(30) + "->\t" + f"Irreducible fraction: ({-b:.9f}".rstrip('0').rstrip('.') + " - √(" + f"{discriminant:.9f}".rstrip('0').rstrip('.') + "))" + " / " f"{denominator:.9f}".rstrip('0').rstrip('.'))
        print(f"{numerator2 / denominator:.9f}".ljust(30) + "->\t" + f"Irreducible fraction: ({-b:.9f}".rstrip('0').rstrip('.') + " + √(" + f"{discriminant:.9f}".rstrip('0').rstrip('.') + "))" + " / " f"{denominator:.9f}".rstrip('0').rstrip('.'))
        print(f"{numerator1 / denominator:.9f}".ljust(30) + "->\t" + f"{decimal_to_fraction(-b / denominator)}".rstrip('0').rstrip('.') + " - (√(" + f"{discriminant:.9f}".rstrip('0').rstrip('.') + "))" + " / " f"{denominator:.9f}".rstrip('0').rstrip('.') + ")")
        print(f"{numerator2 / denominator:.9f}".ljust(30) + "->\t" + f"{decimal_to_fraction(-b / denominator)}".rstrip('0').rstrip('.') + " + (√(" + f"{discriminant:.9f}".rstrip('0').rstrip('.') + "))" + " / " f"{denominator:.9f}".rstrip('0').rstrip('.') + ")")                
        return
    print(f"{numerator1 / denominator:.9f}".rstrip('0').rstrip('.').ljust(20) + "->\t" + decimal_to_fraction(numerator1 / denominator))
    print(f"{numerator2 / denominator:.9f}".rstrip('0').rstrip('.').ljust(20) + "->\t" + decimal_to_fraction(numerator2 / denominator))


#accept a third argument to print_results
if (len(sys.argv) < 2 or len(sys.argv) > 3 or ((len(sys.argv) == 3 and sys.argv[2] != '/s'))):
    print("Invalid number of arguments")
    print("Usage: python3 computor.py \"equation\"")
    exit(1)

def parser(arguments):
    identity_sides = pre_parser(arguments)
    # Split on '+' or '-' while keeping the sign (lookahead assertion)
    left_terms = re.split(r'(?=[+-])', identity_sides[0])
    right_terms = re.split(r'(?=[+-])', identity_sides[1])
    # Filter out any empty strings from the lists
    left_terms = [term for term in left_terms if term]
    right_terms = [term for term in right_terms if term]
    print(identity_sides, left_terms, right_terms, len(left_terms), len(right_terms))
    #hacer un post parser que no permita para empezar un exponente decimal
    for terms in chain(left_terms, right_terms):
        if re.search(r'[xX]\^\d+\.\d+', terms):
            raise ValueError("Exponentials must be integers")
    for terms in left_terms:
        match = re.findall(r'([+-]?\d*\.?\d*)\*[xX]\^(\d+)', terms)
        print(match)   
    for terms in right_terms:
        match = re.findall(r'([+-]?\d*\.?\d*)\*[xX]\^(\d+)', terms)
        print(match)
    coefficients = []
    for argument in arguments.split(" "):
        coefficients.append(float(argument))
    return coefficients

#hacer un post parser que no permita para empezar un exponente decimal
for terms in chain(left_terms, right_terms):
    if re.search(r'[xX]\^\d+\.\d+', terms):
        raise ValueError("Exponentials must be integers")