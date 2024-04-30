"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether the given month number contains 31 days or not.
'''

def check_monthnumb_number(monthnum2):
  if monthnum2 in [1,3,5,7,8,10,12]:
    return True
  else:
    return False

'''
Standard answer: 
def check_monthnumb_number(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
'''
assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(6)==False
