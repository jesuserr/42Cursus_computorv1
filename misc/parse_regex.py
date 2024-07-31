'''To parse identity_sides and obtain the coefficients and exponents, you can follow these steps:

- Split the equation into left and right sides.
- Extract terms from both sides.
- Parse each term to identify the coefficient and exponent.
- Combine terms from both sides to form a unified list of coefficients.

Here's how you can implement this:

Pseudocode

- Split the equation into left and right sides.
- Initialize a dictionary to store coefficients by their exponents.
- For each side:
        Split into terms.
        For each term:
            Extract the coefficient and exponent.
            Adjust the sign based on the side of the equation.
            Update the dictionary with the coefficient.
- Convert the dictionary to a list of coefficients.

Implementation'''

import re
import sys

def parse_term(term):
    match = re.match(r'([+-]?\d*\.?\d*)\*?[xX]\^?(\d*)', term)
    if match:
        coefficient = match.group(1)
        exponent = match.group(2)
        coefficient = float(coefficient) if coefficient not in ["", "+", "-"] else float(coefficient + "1")
        exponent = int(exponent) if exponent else 1
    else:
        coefficient = float(term)
        exponent = 0
    return coefficient, exponent

def parser_2(arguments):
    allowed_chars = "0123456789*+-xX^=. "
    if not all(char in allowed_chars for char in arguments):
        raise ValueError("Invalid characters in input")
    arguments_no_blanks = arguments.replace(" ", "")
    invalid_sequences = ["**", "++", "--", "xx", "XX", "xX", "Xx" , "^^", "=="]
    invalid_sequences += ["..", "+-", "-+"]
    for seq in invalid_sequences:
        if seq in arguments_no_blanks:
            raise ValueError(f"Invalid sequence found: {seq}")
    identity_sides = arguments_no_blanks.split("=")
    if len(identity_sides) != 2:
        raise ValueError("Invalid number of equal signs")
    if identity_sides[0] == "" or identity_sides[1] == "":
        raise ValueError("Invalid number of expressions")        
    return identity_sides

def parser(arguments):
    identity_sides = parser_2(arguments)
    coefficients = {}
    
    for side, sign in zip(identity_sides, [1, -1]):
        terms = re.split(r'(?=[+-])', side)
        for term in terms:
            if term:
                coefficient, exponent = parse_term(term)
                if exponent in coefficients:
                    coefficients[exponent] += sign * coefficient
                else:
                    coefficients[exponent] = sign * coefficient
    
    max_exponent = max(coefficients.keys())
    coefficient_list = [coefficients.get(i, 0) for i in range(max_exponent + 1)]
    
    return coefficient_list

################################# MAIN FUNCTION ################################

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: python3 computor.py \"equation\"")
        exit(1)
    
    equation = sys.argv[1]
    coefficients = parser(equation)
    print(coefficients)


    #This code will parse the input equation, extract the coefficients and exponents,
    #  and return a list of coefficients. The parse_term function uses regular
    #  expressions to handle different term formats, and the parser function
    #  combines terms from both sides of the equation.