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

def print_arithmetic(t, a, b):
    arith = {"addition":"+", "subtraction":"-", "multiplication":"*", "division":"/", "modulo":"%","floor":"//","ceil":"//"}
    if check_key(arith, t):
        message = t + " : " + str(a) + " " + arith[t] + " " + str(b) + " = "
        if t == "ceil":
            return message + str(eval("-(-" + str(a) + arith[t] + str(b) + ")"))
        else:
            return message + str(eval(str(a) + arith[t] + str(b)))
    else:
        return "Error: arithmetic entered is invalid."

# Driver Code

# Addtition
print(print_arithmetic("addition",2,2))
# Subtraction
print(print_arithmetic("subtraction",5,2))
# Multiplication
print(print_arithmetic("multiplication",3,3))
# Division
print(print_arithmetic("division",10,2))
# Modulo
print(print_arithmetic("modulo",7,4))
# Floor
print(print_arithmetic("floor",5,4))
# Ceil
print(print_arithmetic("ceil",4,3))
# ERROR TEST
print(print_arithmetic("test",8,8)) 
