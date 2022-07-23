from art import logo
# Add
def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

OPERATIONS  = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


# function = OPERATIONS["+"]
# value = function(2,3)

# print(f"{value}") 

def calculator():
  calculating = True
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  
  while calculating:
    for symbol in OPERATIONS:
      print(symbol)
    
    operation_symbol = input("Pick an operatioan from the line above: ")
    
    num2 = float(input("What's the next number?: "))
    
    calculation_function = OPERATIONS[operation_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if  input(f"Type 'y' to continue calculationg with {answer}, or type 'n' to exit. :") == 'n':
      calculating = False
    num1= answer


calculator()