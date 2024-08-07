import re
from itertools import chain

def pre_parser(arguments):
    allowed_chars = "0123456789*+-xX^=. "
    if not all(char in allowed_chars for char in arguments):
        raise ValueError("Invalid characters in input")
    if re.search(r'(\d+|\.+)\s+(\d+|\.+)', arguments):
        raise ValueError("Invalid digits separation")
    arguments_no_blanks = arguments.replace(" ", "")
    invalid_sequences = ["**", "++", "--", "xx", "XX", "xX", "Xx" , "^^", "=="]
    invalid_sequences += ["..", "+-", "-+", "^-", "^+", "-*", "+*", "*-", "*+"]
    invalid_sequences += ["-^", "+^"]
    for seq in invalid_sequences:
        if seq in arguments_no_blanks:
            raise ValueError(f"Invalid sequence found: {seq}")
    identity_sides = arguments_no_blanks.split("=")
    if len(identity_sides) != 2 or not identity_sides[0] or not identity_sides[1]:
        raise ValueError("Invalid number of identities")
    return identity_sides

def find_max_degree(left_terms, right_terms):
    max_degree = 0
    for term in chain(left_terms, right_terms):
        if re.search(r'[xX]\^\d+\.\d+', term):
            raise ValueError("Invalid exponent, must be integer")
        match = re.findall(r'[xX]\^(\d+)', term)
        if match and int(match[0]) > max_degree:
            max_degree = int(match[0])
    return max_degree

def parser(arguments):
    identity_sides = pre_parser(arguments)
    left_terms = re.split(r'(?=[+-])', identity_sides[0])
    right_terms = re.split(r'(?=[+-])', identity_sides[1])
    left_terms = [term for term in left_terms if term]
    right_terms = [term for term in right_terms if term]
    max_degree = find_max_degree(left_terms, right_terms)
    coefficients = [0.0] * max(3, max_degree + 1)
    for term in chain(left_terms, right_terms):
        match = re.findall(r'^([+-]?\d*\.?\d*)\*[xX]\^(\d+)$', term)
        if match and len(match[0]) == 2:
            coefficient = float(match[0][0])
            if term in right_terms:
                coefficient *= -1
            coefficients[int(match[0][1])] += coefficient
        else:
            raise ValueError(f"Invalid term format: {term}")
    #print(identity_sides, left_terms, right_terms, len(left_terms), len(right_terms))
    #print(max_degree, coefficients)
    return coefficients, max_degree