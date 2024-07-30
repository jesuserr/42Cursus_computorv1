class ParserError(Exception):
	pass

class Parser():

	@staticmethod
	def check_equal(av):
		equalfound = False
		for i in range(len(av)):
			if av[i] == '=':
				if equalfound:
					raise ParserError("Found more than one equal sign.")
				equalfound = True
		if not equalfound:
			raise ParserError("No equal sign found.")

	@staticmethod
	def parse(av):
		Parser.check_equal(av)
		i = 0
		number = 0
		sign = 1
		equal = 1
		grades = {'1': 0, '2': 0, '0': 0}
		term = None
		prev_term = None
		if av[0] == '-':
			sign = -1
			i += 1
		while i < len(av) and av[i] == ' ':
			i += 1
		if i == len(av):
			raise ParserError("No number found.")
		while i < len(av):
			# print('i:',i, av[i], 'len', len(av))
			while i < len(av) and av[i] == ' ':
				i += 1
			# parse after equal
			if av[i] == '=':
				equal = -1
				i += 1
				while i < len(av) and av[i] == ' ':
					i += 1
				if i == len(av):
					raise ParserError("No number found after equal sign.")
				if av[i] == '-':
					sign = -1
					i += 1
				if av[i] == '+':
					i += 1
				while i < len(av) and av[i] == ' ':
					i += 1
				if i == len(av):
					raise ParserError("No number found after equal sign.")
			#get number
			if av[i].isdigit():
				# print('entro')	
				dot = False
				grade = 0
				oGrade = True
				# get the number
				while i < len(av) - 1 and av[i].isdigit() or av[i] == '.':
					if av[i] == '.':
						if dot:
							raise ParserError("Found more than one dot in a single number.")
						dot = True
						
					else:
						if dot:
							number += float(av[i]) / 10
						else:
							number = number * 10 + float(av[i])
					i += 1
				if i == len(av) - 1 and av[i].isdigit():
					number = number * 10 + float(av[i])
					# print(i, len(av), av[i])
				# remove spaces after it
				while i < len(av) and av[i] == ' ':
					i += 1
				if i < len(av) and av[i] == '*':
					i += 1
				while i < len(av) and av[i] == ' ':
					i += 1
				# check if there is a grade
				if i < len(av) and (av[i] == 'x' or av[i] == 'X'):
					i += 1
					# print('xgrade', av[i])
					# print('entrooooo')
					while i < len(av) and av[i] == ' ':
						i += 1
					if i < len(av) and av[i] != '+' and av[i] != '-' and av[i] != '=':
						if i < len(av) and av[i] == '^':
							i += 1
							while i < len(av) and av[i] == ' ':
								i += 1
							if i < len(av) and av[i].isdigit():
								while i < len(av) and av[i].isdigit():
									oGrade = False
									grade = grade * 10 + int(av[i])
									i += 1
							else:
								raise ParserError("Invalid grade.")
						else:
							raise ParserError("Invalid grade format.")
					if grade == 0 and oGrade:
						grade = 1
				# print('number: ', number, grade, sign, equal)
				grades[str(grade)] = grades.get(str(grade), 0) + number * sign * equal
				sign = 1
				grade = 0
				number = 0
			
			if i < len(av) and (av[i] == 'x' or av[i] == 'X'):
				i += 1
				grade = 0

				# print('xgrade', av[i])
				# print('entrooooo')
				if i < len(av) and av[i] != ' ' and av[i] != '+' and av[i] != '-' and av[i] != '=':
					if i < len(av) and av[i] == '^':
						i += 1
						if i < len(av) and av[i].isdigit():
							while i < len(av) and av[i].isdigit():
								grade = grade * 10 + int(av[i])
								i += 1
						else:
							raise ParserError("Invalid grade.")
					else:
						raise ParserError("Invalid grade format.")
				if grade == 0:
					grade = 1
				number = 1
				# print('number: ', number, grade, sign, equal)
				grades[str(grade)] = grades.get(str(grade), 0) + number * sign * equal
				sign = 1
				grade = 0
				number = 0



			if i < len(av) and (av[i] == '+' or av[i] == '-'):
				if av[i] == '-':
					sign = -1
				else:
					sign = 1
				i += 1
				if i == len(av):
					raise ParserError("No number found after sign.")
				term = ''
				continue
			if i >= len(av) - 1:
				# print('last ---------------------------', av[i])
				if not av[- 1].isdigit() and av[-1] != 'x' and av[-1] != 'X' and av[-1] != ' ':
					raise ParserError(f"Invalid last character {av[-1]}.")
				break
			term = av[i] + str(i)
			if term == prev_term:
				raise ParserError(f"Invalid character {av[i]}. {i}")
			prev_term = term
		


		
		sorted_grades = {k: v for k, v in sorted(grades.items(), key=lambda item: int(item[0])) if v != 0}
		
		formatted_grades = " + ".join([f"{v} * X ^ {k}" if int(k) != 0 else str(v) for k, v in sorted_grades.items()])

		
		highest_key = None

		formatted_grades = formatted_grades.replace(" + -", " - ")
		for key, value in grades.items():
			if value != 0:
				if highest_key is None or int(key) > int(highest_key):
					highest_key = key


		# if highest_key is not None:
		# 	print(f"The highest key with a relevant value is: {highest_key}")
		# else:
		# 	print("No key with a relevant value found.")

		if formatted_grades != "":
			print("Reduced form:", formatted_grades, "= 0")
		else:
			print("0 = 0")
		# print(grades)
		if highest_key is not None and int(highest_key) > 2:
			print(f"Polinomial degree: {highest_key}")
			print("The polynomial degree is stricly greater than 2, I can't solve.")
			exit(0)
		else:
			print(f"Polinomial degree: {highest_key}")
		return grades['2'], grades['1'], grades['0'], highest_key


if __name__ == "__main__":
	try:
		Parser.parse("1.0 * x^0 +   2.0x  - 09.0x^2  = -3")
	except Exception as e:
		print(e)
		
		
		
		
	
