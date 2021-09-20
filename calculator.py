# calculator.py
# Aarsh Shah, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#


'''
Function that asks the user for 
'''
#
user_num1 = int(input('Enter in the 1st integer value'))
user_exp1 = input('Enter in expression that will occur between value 1 and 2')
user_num2 = int(input('Enter in the 2nd integer Value'))
user_num1 = input('Enter in expression that will occur between the answer of the first operation and the 3rd number')
user_exp2 = int(input('Enter in the 3rd integer Value'))

if user_exp1 == '*':
    answer1 = user_num1 * user_num2

elif user_exp1 =='/':
    answer1 = user_num1 / user_num2

elif user_exp1 == '+':
    answer1 = user_num1 + user_num2

elif user_exp1 == '-':
    answer1 = user_num1 - user_num2
else:
    print("Expression not supported")


if user_exp1 == '*':
    final_answer = answer1 * user_num2

elif user_exp1 =='/':
    final_answer = user_num1 / user_num2

elif user_exp1 == '+':
    final_answer = user_num1 + user_num2

elif user_exp1 == '-':
    final_answer = user_num1 - user_num2
else:
    print("Expression not supported")




