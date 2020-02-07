"""
numbers.py

Review how numbers and arithmetic are performed in Python
added two helper functions to return mathematical expressions.
"""

def check_key(dict, key):
    if key in dict.keys():
        return key
    else:
        return False

def print_arithmetic(t, a, b=0.5):
    arith = {"addition":"+", "subtraction":"-", "multiplication":"*", "division":"/", "modulo":"%"
            ,"floor":"//","ceil":"//","power":"**","square":"**"}
    if check_key(arith, t):
        message = t + " : " + str(a) + " " + arith[t] + " " + str(b) + " = "
        if t == "ceil":
            return message + str(eval("-(-" + str(a) + arith[t] + str(b) + ")"))
            # return -(-a//b)
        else:
            
            return message + str(eval(str(a) + arith[t] + str(b)))
    else:
        return "Error: arithmetic entered is invalid."

# Driver Code
if __name__ == '__main__':
  print_arithmetic("addition",2,2)
  # Subtraction
  print_arithmetic("subtraction",5,2)
  # Multiplication
  print_arithmetic("multiplication",3,3)
  # Division
  print_arithmetic("division",10,2)
  # Modulo
  print_arithmetic("modulo",7,4)
  # Floor
  print_arithmetic("floor",5,4)
  # Ceil
  print_arithmetic("ceil",4,3)
  # Power
  print_arithmetic("power",2,4)
   # Square
  print_arithmetic("square",4)
  # ERROR TEST
  print_arithmetic("test",8,8)  
