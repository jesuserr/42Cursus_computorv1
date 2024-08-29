import re
import argparse
import sys
from itertools import chain
#from fractions import Fraction

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
    #return (f"{Fraction(number).limit_denominator()}")
    integer_part = int(number)
    fractional_part = number - integer_part
    precision = 1000000000
    gcd_value = gcd(round(fractional_part * precision), precision)
    numerator = round(fractional_part * precision) // gcd_value
    denominator = precision // gcd_value
    return f"{(integer_part * denominator) + numerator} / {denominator}"

def parse_arguments():
    # Trick to avoid argparse error for negative numbers on equation with no spaces
    if len(sys.argv) > 1:
        sys.argv[1] = sys.argv[1] + " "
    msg = "python3 computor.py equation [-p] [-s] [-i]\n"
    msg += "equation: e.g. \"4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0\"\n"
    msg += "[-p]: plot the equation\n"
    msg += "[-s]: show intermediate steps\n"
    msg += "[-i]: show irreducible fractions"
    arg_parser = argparse.ArgumentParser(add_help=False, usage=msg)
    arg_parser.add_argument('equation', type=str)
    arg_parser.add_argument("-p", '--plot', action='store_true')
    arg_parser.add_argument('-s', '--steps', action='store_true')
    arg_parser.add_argument('-i', '--irreducible', action='store_true')
    args = arg_parser.parse_args()
    if any(arg.startswith('-') and len(arg) > 2 for arg in sys.argv[2:]):
        print("usage: " + msg)
        print("computor.py: error: unrecognized arguments")
        sys.exit(1)
    return args