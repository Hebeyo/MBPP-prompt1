"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find minimum of three numbers.
'''

def min_of_three(a,b,c): 
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c

'''
Standard answer: 
def min_of_three(a,b,c): 
      if (a <= b) and (a <= c): 
        smallest = a 
      elif (b <= a) and (b <= c): 
        smallest = b 
      else: 
        smallest = c 
      return smallest 
'''
assert min_of_three(10,20,0)==0
assert min_of_three(19,15,18)==15
assert min_of_three(-10,-20,-30)==-30
