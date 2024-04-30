"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to print positive numbers in a list.
'''

def pos_nos(list1):
  for num in list1: 
    if num >= 0: 
       return num

'''
Standard answer: 
def pos_nos(list1):
  for num in list1: 
    if num >= 0: 
       return num 
'''
assert pos_nos([-1,-2,1,2]) == 1,2
assert pos_nos([3,4,-5]) == 3,4
assert pos_nos([-2,-3,1]) == 1
