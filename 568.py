"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to create a list of empty dictionaries.
'''

def empty_list(length):
  empty_list = []
  for i in range(length):
    empty_list.append({})
  return empty_list

'''
Standard answer: 
def empty_list(length):
 empty_list = [{} for _ in range(length)]
 return empty_list
'''
assert empty_list(5)==[{},{},{},{},{}]
assert empty_list(6)==[{},{},{},{},{},{}]
assert empty_list(7)==[{},{},{},{},{},{},{}]
