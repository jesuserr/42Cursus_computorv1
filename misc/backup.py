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