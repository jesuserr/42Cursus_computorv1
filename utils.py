import re
import argparse
import sys
from itertools import chain

def find_max_degree(left_terms, right_terms):
    max_degree = 0
    for term in chain(left_terms, right_terms):
        if re.search(r'[xX]\^\d+\.\d+', term):
            raise ValueError("Invalid exponent, must be integer")
        match = re.findall(r'[xX]\^(\d+)', term)
        if match and int(match[0]) > max_degree:
            max_degree = int(match[0])
    return max_degree

def strip(number, justify=0, default_precision=".9f"):
    if number == -0:
        number = 0
    return f"{number:{default_precision}}".rstrip('0').rstrip('.').ljust(justify)

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

def parse_arguments():
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('equation', type=str)
    arg_parser.add_argument("-p", '--plot', action='store_true')
    arg_parser.add_argument('-s', '--steps', action='store_true')
    args = arg_parser.parse_args()
    if any(arg.startswith('-') and len(arg) > 2 for arg in sys.argv[1:]):
        print("usage: computor.py [-p] [-s] equation")
        print("computor.py: error: unrecognized arguments")
        sys.exit(1)
    return args