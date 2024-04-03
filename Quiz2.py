# Question 1:
"""
    Try to print a variable that is not yet defined. 
    If a NameError exception is thrown, then print 
    'This variable is not yet defined'
"""
try:
    print(hello)
except NameError:
    print("This variable is not yet defined")


# Question 2:
"""
    Have a person input a formula that consist of 
    a number, an operator (at least + and -), and another number, 
    separated by white space (e.g. 1 + 1). If the middle inputted
    item is not a '+' or a '-' then raise a custom
    CantHandleOperand error. 
"""
class CantHandleOperand(Exception):
   pass
formula = input("Please enter a formula: Make sure theres a number, an operator, and another number")
formula_list = formula.split()
if formula_list[1] != '+' or formula_list[1] != '-':
    raise CantHandleOperand
x