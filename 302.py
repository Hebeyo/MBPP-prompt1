"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the most significant bit number which is also a set bit.
'''

def set_Bit_Number(n): 
    if (n == 0): 
        return 0; 
    msb = 0; 
    n = int(n / 2); 
    while (n > 0): 
        n = int(n / 2); 
        msb += 1; 
    return (1 << msb)

'''
Standard answer: 
def set_Bit_Number(n): 
    if (n == 0): 
        return 0; 
    msb = 0; 
    n = int(n / 2); 
    while (n > 0): 
        n = int(n / 2); 
        msb += 1; 
    return (1 << msb)
'''
assert set_Bit_Number(6) == 4
assert set_Bit_Number(10) == 8
assert set_Bit_Number(18) == 16
