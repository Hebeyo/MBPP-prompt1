"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to accept the strings which contains all vowels.
'''

def check(string): 
  count=0
  for i in string: 
    if i in 'AEIOUaeiou': 
      count+=1
    if count>=5: 
      return 'accepted'
  return 'not accepted'

'''
Standard answer: 
def check(string): 
  if len(set(string).intersection("AEIOUaeiou"))>=5: 
    return ('accepted') 
  else: 
    return ("not accepted") 
'''
assert check("SEEquoiaL") == 'accepted'
assert check('program') == "not accepted"
assert check('fine') == "not accepted"
