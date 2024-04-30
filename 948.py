"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to get an item of a tuple.
'''

def get_item(tup1,index):
  item = tup1[index]
  return item

'''
Standard answer: 
def get_item(tup1,index):
  item = tup1[index]
  return item
'''
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==('e')
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-4)==('u')
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-3)==('r')
