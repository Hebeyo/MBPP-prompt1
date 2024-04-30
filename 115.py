"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether all dictionaries in a list are empty or not.
'''

def empty_dit(list1):
 for d in list1:
  if d:
   return False
 return True

'''
Standard answer: 
def empty_dit(list1):
 empty_dit=all(not d for d in list1)
 return empty_dit
'''
assert empty_dit([{},{},{}])==True
assert empty_dit([{1,2},{},{}])==False
assert empty_dit({})==True
