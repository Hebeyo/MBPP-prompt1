"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count lower case letters in a given string.
'''

def lower_ctr(str):
    return sum(1 for i in str if i.islower())

'''
Standard answer: 
def lower_ctr(str):
      lower_ctr= 0
      for i in range(len(str)):
          if str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1     
      return  lower_ctr
'''
assert lower_ctr('abc') == 3
assert lower_ctr('string') == 6
assert lower_ctr('Python') == 5
