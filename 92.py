"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether the given number is undulating or not.
'''

def is_undulating(n):
  if len(n) < 3:
    return False
  for i in range(2, len(n)):
    if n[i-2] != n[i]:
      return False
  return True

'''
Standard answer: 
def is_undulating(n): 
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
'''
assert is_undulating("1212121") == True
assert is_undulating("1991") == False
assert is_undulating("121") == True
