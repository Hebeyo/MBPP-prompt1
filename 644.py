"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to reverse an array upto a given position.
'''

def reverse_Array_Upto_K(input, k): 
  return (input[k-1::-1] + input[k:])

'''
Standard answer: 
def reverse_Array_Upto_K(input, k): 
  return (input[k-1::-1] + input[k:]) 
'''
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]
