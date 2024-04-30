"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find smallest number in a list.
'''

def smallest_num(xs):
  min = xs[0]
  for i in xs:
    if i < min:
      min = i
  return min

'''
Standard answer: 
def smallest_num(xs):
  return min(xs)

'''
assert smallest_num([10, 20, 1, 45, 99]) == 1
assert smallest_num([1, 2, 3]) == 1
assert smallest_num([45, 46, 50, 60]) == 45
