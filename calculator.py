# calculator.py
# Aarsh Shah, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#

# Asks user to input the first integer variable and stores in a variable
user_num1 = int(input('Enter in the 1st integer value: '))
# Asks user to input the first operator and stores in a variable
user_exp1 = input(
    'Enter in expression that will occur between value 1 and 2 (*, /, +, -): ')
# Asks user to input the second integer variable and stores in a variable
user_num2 = int(input('Enter in the 2nd integer Value: '))
# Asks user to input the second operator and stores in a variable
user_exp2 = input(
    'Enter in expression that will occur between the answer of the first operation and the 3rd number (*, /, +, -): ')
# Asks user to input the third integer variable and stores in a variable
user_num3 = int(input('Enter in the 3rd integer Value: '))


# Checks if the first operator chosen is multiplication
if user_exp1 == '*':
    answer1 = user_num1 * user_num2
# Checks if the first operator chosen is division
elif user_exp1 == '/':
    answer1 = user_num1 / user_num2
# Checks if the first operator chosen is adding
elif user_exp1 == '+':
    answer1 = user_num1 + user_num2
# Checks if the first operator chosen is subtraction
elif user_exp1 == '-':
    answer1 = user_num1 - user_num2
# If the expression chosen is not one of the listed above it returns
# a statement saying the operator is not supported by the code
else:
    print("Expression not supported")


# Checks if the second operator chosen is multiplication
if user_exp2 == '*':
    final_answer = answer1 * user_num3
# Checks if the second operator chosen is division
elif user_exp2 == '/':
    final_answer = answer1 / user_num3
# Checks if the second operator chosen is addition
elif user_exp2 == '+':
    final_answer = answer1 + user_num3
# Checks if the second operator chosen is subtraction
elif user_exp2 == '-':
    final_answer = answer1 - user_num3
# If the expression chosen is not one of the listed above it returns
# a statement saying the operator is not supported by the code
else:
    print("Expression not supported")


# Prints the full expression entered by the user while converting the variables to strings
print('Entered Expression:', str(user_num1), str(user_exp1),
      str(user_num2), str(user_exp2), str(user_num3))
# Prints the final answer of the calculations while converting it to a string
print('Final Answer:', (int(final_answer)))
