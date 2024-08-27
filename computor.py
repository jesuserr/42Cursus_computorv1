import sys
from parser import parser
from solver import solver
from plot import plot
from utils import parse_arguments

if __name__ == '__main__':
    args = parse_arguments()
    try:
        coefficients = parser(args.equation)
        solver(coefficients, args.steps, args.irreducible)
        plot(coefficients) if args.plot else None
    except ValueError as error:
        print(error)
        sys.exit(1)