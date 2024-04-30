"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check a decimal with a precision of 2.
'''

def is_decimal(num):
    if num.isdigit():
        return True
    num = num.split('.')
    if len(num) != 2:
        return False
    if not num[0].isdigit() or not num[1].isdigit():
        return False
    if len(num[1]) != 2:
        return False
    return True

'''
Standard answer: 
def is_decimal(num):
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)
'''
assert is_decimal('123.11')==True
assert is_decimal('e666.86')==False
assert is_decimal('3.124587')==False
