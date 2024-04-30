"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether the given month number contains 30 days or not.
'''

def check_monthnumber_number(monthnum3):
  if(monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11):
    return True
  else:
    return False

'''
Standard answer: 
def check_monthnumber_number(monthnum3):
  if(monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11):
    return True
  else:
    return False
'''
assert check_monthnumber_number(6)==True
assert check_monthnumber_number(2)==False
assert check_monthnumber_number(12)==False
