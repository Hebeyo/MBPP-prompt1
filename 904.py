"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to return true if the given number is even else return false.
'''

def even_num(x):
  if x%2==0:
     return True
  else:
    return False

'''
Standard answer: 
def even_num(x):
  if x%2==0:
     return True
  else:
    return False
'''
assert even_num(13.5)==False
assert even_num(0)==True
assert even_num(-9)==False
