"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether all the bits are within a given range or not.
'''

def all_Bits_Set_In_The_Given_Range(n,l,r):
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
    new_num = n & num
    if (num == new_num):
        return True
    return False

'''
Standard answer: 
def all_Bits_Set_In_The_Given_Range(n,l,r): 
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 
    new_num = n & num 
    if (num == new_num): 
        return True
    return False
'''
assert all_Bits_Set_In_The_Given_Range(10,2,1) == True 
assert all_Bits_Set_In_The_Given_Range(5,2,4) == False
assert all_Bits_Set_In_The_Given_Range(22,2,3) == True 
