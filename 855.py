"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check for even parity of a given number.
'''

def check_Even_Parity(x): 
    return bin(x).count('1') % 2 == 0

'''
Standard answer: 
def check_Even_Parity(x): 
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    if (parity % 2 == 0): 
        return True
    else: 
        return False
'''
assert check_Even_Parity(10) == True
assert check_Even_Parity(11) == False
assert check_Even_Parity(18) == True
