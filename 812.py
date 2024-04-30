"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to abbreviate 'road' as 'rd.' in a given string.
'''

def road_rd(street):
  return street.replace('Road','Rd.')

'''
Standard answer: 
import re
def road_rd(street):
  return (re.sub('Road$', 'Rd.', street))
'''
assert road_rd("ravipadu Road")==('ravipadu Rd.')
assert road_rd("palnadu Road")==('palnadu Rd.')
assert road_rd("eshwar enclave Road")==('eshwar enclave Rd.')
