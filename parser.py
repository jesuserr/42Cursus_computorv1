import re
from utils import find_max_degree

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

def parser(arguments):
    identity_sides = pre_parser(arguments)
    left_terms = re.split(r'(?=[+-])', identity_sides[0])
    right_terms = re.split(r'(?=[+-])', identity_sides[1])
    left_terms = [term for term in left_terms if term]
    right_terms = [term for term in right_terms if term]
    max_degree = find_max_degree(left_terms, right_terms)
    # Initialize coefficients list with zeros and minimum size of 3
    coefficients = [0.0] * max(3, max_degree + 1)
    for term in left_terms:
        match = re.findall(r'^([+-]?\d*\.?\d*)\*[xX]\^(\d+)$', term)
        if match and len(match[0]) == 2:
            coefficients[int(match[0][1])] += float(match[0][0])
        else:
            free_form_parser(term, coefficients, side="left_term")
    for term in right_terms:
        match = re.findall(r'^([+-]?\d*\.?\d*)\*[xX]\^(\d+)$', term)
        if match and len(match[0]) == 2:
            coefficients[int(match[0][1])] += -1 * float(match[0][0])
        else:
            free_form_parser(term, coefficients, side="right_term")
    return coefficients, max_degree

def free_form_parser(term, coefficients, side):
    if re.search(r'^([+-]?\d*\.?\d*)$', term):          # Single coeff. ("4")
        coefficient = float(term)
        if side == "right_term":
            coefficient *= -1
        coefficients[0] += coefficient
    elif re.search(r'^[+-]?[xX]$', term):               # Single x term ("x")
        match = re.findall(r'^([+-]?)[xX]$', term)
        if (side == "right_term" and match[0] == "-") or \
        (side == "left_term" and match[0] == "+"):
            coefficients[1] += 1
        else:
            coefficients[1] -= 1
    elif re.search(r'^[+-]?\d*\.?\d*\*[xX]$', term):    # Absent power ("3*x")
        match = re.findall(r'^([+-]?\d*\.?\d*)\*[xX]$', term)
        coefficient = float(match[0])
        if side == "right_term":
            coefficient *= -1
        coefficients[1] += coefficient
    elif re.search(r'^([+-]?)[xX]\^(\d+)$', term):      # Absent coeff. ("x^2")
        match = re.findall(r'^([+-]?)[xX]\^(\d+)$', term)
        coefficient = 1
        if (side == "right_term" and match[0][0] != "-") or \
        (side == "left_term" and match[0][0] == "-"):
            coefficient = -1
        coefficients[int(match[0][1])] += coefficient
    else:
        raise ValueError(f"Invalid term format: {term}")