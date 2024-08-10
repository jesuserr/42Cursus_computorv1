import sys
import argparse
from parser import parser
from solver import solver
from plot import plot

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('equation', type=str)
    arg_parser.add_argument("-p", '--plot', action='store_true')
    arg_parser.add_argument('-s', '--steps', action='store_true')
    args = arg_parser.parse_args()    
    if any(arg.startswith('-') and len(arg) > 2 for arg in sys.argv[1:]):
        print("usage: computor.py [-p] [-s] equation")
        print("computor.py: error: unrecognized arguments")
        sys.exit(1)    
    try:
        coefficients, max_degree = parser(args.equation)
        solver(coefficients, max_degree, args.steps)
        plot(coefficients) if args.plot else None
    except ValueError as error:
        print(error)
        sys.exit(1)

# "2x^2-5x+3=0"     -> two solutions
# python3 computor.py "3 * X^0 -5 * X^1 + 2 * X^2 = 0 * x^0"

# "x^2-4x+4=0"      -> two identical solutions
# python3 computor.py "4 * X^0 - 4 * X^1 + 1 * X^2 = 0 * x^0"

# "x^2-10x+25=0"    -> two identical solutions
# python3 computor.py "25 * X^0 - 10 * X^1 + 1 * X^2 = 0 * x^0"

# "x^2-4x+5=0"      -> complex
# python3 computor.py "5 * X^0 - 4 * X^1 + 1 * X^2 = 0 * x^0"

# "x^2-x+1=0"       -> complex
# python3 computor.py "1 * X^0 - 1 * X^1 + 1 * X^2 = 0 * x^0"

# 3x^2-10x+7=0 (7/3 , 1) no da exacta la fraccion
# python3 computor.py "3*x^2-10*x+7=0"
# 3x^2-2x=0 (0, 2/3) no da exacta la fraccion
# python3 computor.py "3*x^2-2*x=0"

# SUBJECT
# python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"
# python3 computor.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# python3 computor.py "5 + 4 * X + X^2= X^2"