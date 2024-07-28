import sys
from srcs.parser import Parser
from srcs.solver import solve_equation

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Please introduce only 1 argument with correct format.')
		print('Format:')
		print('\"Polinomial equation to be solved with grade up to three\"')
		print('Example:')
		print('\"x^2 -X = 6\"')
		exit(1)
	try:
		a,b,c,highest_key = Parser.parse(sys.argv[1])
	except Exception as e:
		print(e)
		exit(1)
	solve_equation(a, b, c)