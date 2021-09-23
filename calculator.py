# calculator.py
# Aarsh Shah, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#


# Asks user to input the first integer variable and stores in a variable.
user_num1 = int(input('Enter in the 1st integer value: '))
# Asks user to input the first operator and stores it in a variable.
user_exp1 = input('Enter in the first expression (Use: *, /, +, -): ')
# Asks user to input the second integer variable and stores it in a variable.
user_num2 = int(input('Enter in the 2nd integer Value: '))
# Asks user to input the second operator and stores it in a variable.
user_exp2 = input('Enter in the second expression (Use: *, /, +, -): ')
# Asks user to input the third integer value and stores it in a variable.
user_num3 = int(input('Enter in the 3rd integer Value: '))


# Checks if expression 1 is addition or subtraction.
if user_exp1 == '+' or user_exp1 == '-':
    # Checks if expression 1 is multiplication or division.
    if user_exp2 == '*' or user_exp2 == '/':
        # Checks if expression 2 is multiplication.
        if user_exp2 == ('*'):
            # Multiplies 2nd number by the 3rd number.
            answer1 = user_num2 * user_num3
        # Check if expression 2 is division.
        elif user_exp2 == ('/'):
            # Divides the 2nd number by the 3rd number.
            answer1 = user_num2 // user_num3
        # Checks if expression 1 is addition.
        if user_exp1 == ('+'):
            # Adds the 1st number with the answer of the previous expression.
            final_answer = user_num1 + answer1
        # Checks if expression 1 is subtraction.
        elif user_exp1 == ('-'):
            # Subtracts the 1st number with the answer of the previous expression.
            final_answer = user_num1 - answer1


# Checks if expression 1 and 2 is multiplication or division.
if user_exp1 == '*' or user_exp1 == '/':
    if user_exp2 == '*' or user_exp2 == '/':
        # Checks if expression 1 is multiplication.
        if user_exp1 == ('*'):
            # Multiplies 1st number by the 2nd number.
            answer1 = user_num1 * user_num2
        # Checks if expression 1 is division.
        elif user_exp1 == ('/'):
            # Divides the 1st number by the 2nd number.
            answer1 = user_num1 // user_num2
        # Checks if expression 2 is multiplication.
        if user_exp2 == ('*'):
            # Multiplies the answer to the previous expression by the 3rd number.
            final_answer = answer1 * user_num3
        # Checks if expression 2 is division.
        elif user_exp2 == ('/'):
            # Divides the answer to the previous expression by the 3rd number.
            final_answer = answer1 // user_num3


# Checks if expression 1 and 2 are addition or subtraction.
if user_exp1 == '+' or user_exp1 == '-':
    if user_exp2 == '+' or user_exp2 == '-':
        # Checks if expression 1 is addition.
        if user_exp1 == ('+'):
            # Adds the 1st number with the 2nd number.
            answer1 = user_num1 + user_num2
        # Checks if expression 1 is subtraction.
        elif user_exp1 == ('-'):
            # Subtracts the 1st number with the 2nd number.
            answer1 = user_num1 - user_num2
        # Checks if expression 2 is addition.
        if user_exp2 == ('+'):
            # Add answer to the previous expression with the 3rd number.
            final_answer = answer1 + user_num3
        # Checks if expression 2 is subtraction.
        elif user_exp2 == ('-'):
            # Subtracts answer to the previous expression with the 3rd number.
            final_answer = answer1 - user_num3


# Checks expression 1 is multiplication or division.
if user_exp1 == '*' or user_exp1 == ('/'):
    # Checks if expression 2 is addition or subtraction.
    if user_exp2 == ('+') or user_exp2 == ('-'):
        # Checks if expression 1 is multiplication.
        if user_exp1 == ('*'):
            # Multiplies 1st number by the 2nd number.
            answer1 = user_num1 * user_num2
        # Checks if expression 1 is division.
        elif user_exp1 == ('/'):
            # Divides 1st number by the 2nd number.
            answer1 = user_num1 // user_num2
        # Checks if expression 2 is addition.
        if user_exp2 == ('+'):
            # Adds the answer to the previous expression with the 3rd number.
            final_answer = answer1 + user_num3
        # Checks if expression 2 is subtraction.
        elif user_exp2 == ('-'):
            # Subtracts the answer to the previous expression with the 3rd number.
            final_answer = answer1 - user_num3


# Prints the full expression entered by the user while converting the variables to strings.
print('Entered Expression:', str(user_num1), str(user_exp1),
      str(user_num2), str(user_exp2), str(user_num3))
# Prints the final answer of the calculations while converting it to a string.
print('Final Answer:', (str(final_answer)))
