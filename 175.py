"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to verify validity of a string of parentheses.
'''

def is_valid_parenthese(s):
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif i == '}' and stack and stack[-1] == '{':
            stack.pop()
        elif i == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return stack == []

'''
Standard answer: 
def is_valid_parenthese( str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
'''
assert is_valid_parenthese("(){}[]")==True
assert is_valid_parenthese("()[{)}")==False
assert is_valid_parenthese("()")==True
