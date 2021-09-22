# calculator.py
# Aarsh Shah, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#

# Asks user to input the first integer variable and stores in a variable


user_num1 = int(input('Enter in the 1st integer value: '))
# Asks user to input the first operator and stores it in a variable
user_exp1 = input('Enter in the first expression (Use: *, /, +, -): ')
# Asks user to input the second integer variable and stores it in a variable
user_num2 = int(input('Enter in the 2nd integer Value: '))
# Asks user to input the second operator and stores it in a variable
user_exp2 = input('Enter in the second expression (Use: *, /, +, -): ')
# Asks user to input the third integer value and stores it in a variable
user_num3 = int(input('Enter in the 3rd integer Value: '))


if user_exp1 == ('+') or ('-') and user_exp2 == ('*') or ('/'):
    if user_exp2 == ('*'):
        answer1 = user_num2 * user_num3
        if user_exp1 == ('+'):
            final_answer = user_num1 + answer1
        elif user_exp1 == ('-'):
            final_answer = user_num1 - answer1
    elif user_exp2 == ('/'):
        answer1 = user_num2 // user_num3
        if user_exp1 == ('+'):
            final_answer = user_num1 + answer1
        elif user_exp1 == ('-'):
            final_answer = user_num1 - answer1


if user_exp1 and user_exp2 == ('*') or ('/'):
    if user_exp1 == ('*'):
        answer1 = user_num1 * user_num2
    elif user_exp1 == ('/'):
        answer1 = user_num1 // user_num2
    if user_exp2 == ('*'):
        final_answer = answer1 * user_num3
    elif user_exp2 == ('/'):
        final_answer = answer1 // user_num3


if user_exp1 and user_exp2 == ('+') or ('-'):
    if user_exp1 == ('+'):
        answer1 = user_num1 + user_num2
    elif user_exp1 == ('-'):
        answer1 = user_num1 - user_num2
    if user_exp2 == ('+'):
        final_answer = answer1 + user_num3
    elif user_exp2 == ('-'):
        final_answer = answer1 - user_num3


if user_exp1 == ('*') or ('/') and user_exp2 == ('+') or ('-'):
    if user_exp1 == ('*'):
        answer1 = user_num1 * user_num2
    elif user_exp1 == ('/'):
        answer1 = user_num1 // user_num2
    if user_exp2 == ('+'):
        final_answer = answer1 + user_num2
    elif user_exp2 == ('-'):
        final_answer = answer1 - user_num2


# Prints the full expression entered by the user while converting the variables to strings
print('Entered Expression:', str(user_num1), str(user_exp1),
      str(user_num2), str(user_exp2), str(user_num3))
# Prints the final answer of the calculations while converting it to a string
print('Final Answer:', (int(final_answer)))
