import sys
from parser import parser
from solver import solver

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: python3 computor.py \"equation\"")
        exit(1)
    try:
        coefficients = parser(sys.argv[1])
        solver(coefficients)
    except ValueError as error:
        print(error)
        exit(1)

# "2x^2-5x+3=0"     -> two solutions
# python3 computor.py "3 -5 2"

# "x^2-4x+4=0"      -> two identical solutions
# python3 computor.py "4 -4 1"

# "x^2-10x+25=0"    -> two identical solutions
# python3 computor.py "25 -10 1"

# "x^2-4x+5=0"      -> complex
# python3 computor.py "5 -4 1"

# "x^2-x+1=0"       -> complex
# python3 computor.py "1 -1 1"

# python3 computor.py "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
# python3 computor.py "4 4 -9.3"

# 3x^2-10x+7=0 (7/3 , 1) no funciona la fraccion
# 3x^2-2x=0 (0, 2/3) no funciona la fraccion

# que no acepte numero sin x
# python3 computor.py "8 * X^0 = 8" -> error