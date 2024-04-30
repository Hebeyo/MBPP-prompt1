"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to concatenate all elements of the given list into a string.
'''

def concatenate_elements(list):
  ans = ' '
  for i in list:
    ans = ans+ ' '+i
  return (ans)

'''
Standard answer: 
def concatenate_elements(list):
  ans = ' '
  for i in list:
    ans = ans+ ' '+i
  return (ans) 
'''
assert concatenate_elements(['hello','there','have','a','rocky','day'] ) == '  hello there have a rocky day'
assert concatenate_elements([ 'Hi', 'there', 'How','are', 'you'] ) == '  Hi there How are you'
assert concatenate_elements([ 'Part', 'of', 'the','journey', 'is', 'end'] ) == '  Part of the journey is end'
