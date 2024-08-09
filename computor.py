import sys
from parser import parser
from solver import solver
from plot import plot

if __name__ == '__main__':
    if (len(sys.argv) not in [2, 3] or ((len(sys.argv) == 3 and sys.argv[2] != '-p'))):
        print("Invalid number of arguments")
        print("Usage: python3 computor.py \"equation\" [-p]")
        exit(1)
    try:
        coefficients, max_degree = parser(sys.argv[1])
        solver(coefficients, max_degree)
        if len(sys.argv) == 3 and sys.argv[2] == '-p':
            plot(coefficients)
    except ValueError as error:
        print(error)
        exit(1)

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

'''
Reduced form: 3 * X^2 - 2 * X = 0
Polynomial degree: 2
Variables: a = 3, b = -2, c = 0
Equation form: a * X^2 + b * X + c
Discriminant: 4
Solutions form:
X1 = (-b + sqrt(delta)) / (2 * a)
X2 = (-b - sqrt(delta)) / (2 * a)
Discriminant is stricly positive, the two solutions are:
2 / 3
0
'''