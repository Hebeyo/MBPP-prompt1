"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find out the second most repeated (or frequent) string in the given sequence.
'''

from collections import Counter
def second_frequent(arr):
    count = Counter(arr)
    return sorted(count, key=count.get, reverse=True)[1]

'''
Standard answer: 
from collections import Counter 
	
def second_frequent(input): 
	dict = Counter(input) 
	value = sorted(dict.values(), reverse=True)  
	second_large = value[1] 
	for (key, val) in dict.items(): 
		if val == second_large: 
			return (key) 
'''
assert second_frequent(['aaa','bbb','ccc','bbb','aaa','aaa']) == 'bbb'
assert second_frequent(['abc','bcd','abc','bcd','bcd','bcd']) == 'abc'
assert second_frequent(['cdma','gsm','hspa','gsm','cdma','cdma']) == 'gsm'
