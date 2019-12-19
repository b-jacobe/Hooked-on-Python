"""
valid_parentheses

Given a string containing just characters
'{}' . '[]', '()' determine if the input string
is valid.

Open brackets must be closed by the same type
Open brackets must be closed in the correct order
Empty string is also valid
"""

#Think stack, queues, and elimninations
# Method #1
def isValid(myStr): 
    stack = []
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 
    for character in myStr: 
        if character in open_list: 
            stack.append(character) 
        elif character in close_list: 
            pos = close_list.index(character) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True

# Driver code 
string_1 = "{[]{()}}"
string_2 = "[{}{})(]"
print(string_1,"-", isValid(string_1)) 
print(string_2,"-", isValid(string_2)) 