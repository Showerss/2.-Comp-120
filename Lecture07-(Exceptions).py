# Warm Up: Write out at least two chunks of code that will
# raise some sort of exception in Python. You can have multiple
# lines of code for each exception. 

"""
exception means something isnt allowed within your program
exception is a class itself

try/except block runs code and if it fails, it will run the except block
you can even do multiple except blocks based on what type of error was thrown in the initial try block
it can get into try/except/else/finally blocks
    it can go try - except - finally
    or try - else - finally
it will only do ONE except then finish the entire chunk
always prints finally block

only use try/except if you cant use an if/else statement
    if you can use an if/else statement, use that instead

raise NameOfError('message you want to display')
    raise ValueError('You dead wrong son')
    rause must be made first as a subclass of exception before being used if you want a specific error name
    you can also.. 
        raise Exception('You dead wrong son')

assert statements:
  should always be used at the beginning of the function after docstring
  enforces preconditions of parameters
  very similar to raise
  must be booleans


  if you had 
    def population(pop:int)
    assert pop >= 0 
  
    this would throw an error if population was less than 0 

  just like if...
    if x<0 or x>100
      print('bad grade')
      raise AssertionError

    instead write
    assert 0 <= x <= 100, 'bad grade'



  



"""

# Exercise 1: 
"""
    Try to run the following code. If any exception is thrown, 
    print "an error occurred" 
"""
# Open file in read-only mode
try:
    with open("not_here.txt", 'r') as f:
        f.write("Hello World!")
except:
    print("an error occurred")



# Exercise 2: 
"""
    Write a Python program that prompts the user to input 
    two numbers and raises a TypeError exception if the inputs 
    are not numerical.
"""
try:
    num1 = float(input("Please input a number: "))
    num2 = float(input("Please input a number: "))
except ValueError:
    print("Please use numerals only")



# Exercise 3: 
"""
    Write a Python program that opens a file and handles a 
    FileNotFoundError exception if the file does not exist.
"""
try:
  f = open("DoesNotExist.txt", 'r')
except FileNotFoundError:
  print("file doesn't exist")



# Exercise 4: 
"""
  Write a Python program that executes an operation on a 
  list and handles an IndexError exception if the index 
  is out of range.
"""
class philscustomexception(Exception):
   pass

listA = [1,4545,132,346,-10,2,3]

try:
  print(listA[100])
except:
  raise philscustomexception ("index out of range")


# Exercise 5: 
"""
    You're going to write an interactive calculator! 
    User input is assumed to be a formula that consist of 
    a number, an operator (at least + and -), and another number, 
    separated by white space (e.g. 1 + 1). Split user input 
    using str.split(), and check whether the resulting list is 
    valid:
        1) If the input does not consist of 3 elements, 
           raise a FormulaError, which is a custom Exception.
        2) Try to convert the first and third input to a float 
           (like so: float_value = float(str_value)). Catch any 
           ValueError that occurs, and instead raise a FormulaError
        3) If the second input is not '+' or '-', again raise a 
           FormulaError
"""
class FormulaError(Exception):
   pass

def parse_input(user_input):

  input_list = user_input.split()
  assert len(input_list) == 3
  # TO DO: If the input does not consist of 3 elements, 
  # raise a FormulaError, which is a custom Exception.
  
  n1, op, n2 = input_list
  # TO DO: Try to convert the first and third input to a float 
  # Catch any ValueError that occurs, and instead raise 
  # a FormulaError
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
     raise FormulaError ("Cannot convert to a float")
     


  return n1, op, n2

def calculate(n1, op, n2):


    if op == '+':
      return n1 + n2
    elif op == '-':
      return n1 - n2
    else:
       raise FormulaError

  #   elif op == '*':
  #     return n1 * n2
  #   elif op == '/':
  #     return n1 / n2
  # # TO DO: If the second input is not '+' or '-', again raise a FormulaError
  #   else:
  #     pass

  

while True:
  user_input = input("Please enter the formula, or 'quit': ")
  if user_input == 'quit':
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)