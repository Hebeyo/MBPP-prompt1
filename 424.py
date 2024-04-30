"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to extract only the rear index element of each string in the given tuple.
'''

def extract_rear(test_tuple):
    res = []
    for sub in test_tuple:
        res.append(sub[len(sub) - 1])
    return (res)

'''
Standard answer: 
def extract_rear(test_tuple):
  res = list(sub[len(sub) - 1] for sub in test_tuple)
  return (res) 
'''
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']
