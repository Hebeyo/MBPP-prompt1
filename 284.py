"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether all items of a list are equal to a given string.
'''

def check_element(list,element):
  for i in list:
    if i!=element:
      return False
  return True

'''
Standard answer: 
def check_element(list,element):
  check_element=all(v== element for v in list)
  return check_element
'''
assert check_element(["green", "orange", "black", "white"],'blue')==False
assert check_element([1,2,3,4],7)==False
assert check_element(["green", "green", "green", "green"],'green')==True
