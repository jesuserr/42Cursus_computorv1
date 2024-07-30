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