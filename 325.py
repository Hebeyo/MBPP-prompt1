"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the minimum number of squares whose sum is equal to a given number.
'''

def get_Min_Squares(n):
	if n <= 3:
		return n;
	res = n 
	for x in range(1,n + 1):
		temp = x * x;
		if temp > n:
			break
		else:
			res = min(res,1 + get_Min_Squares(n  - temp)) 
	return res;

'''
Standard answer: 
def get_Min_Squares(n):
    if n <= 3:
        return n;
    res = n 
    for x in range(1,n + 1):
        temp = x * x;
        if temp > n:
            break
        else:
            res = min(res,1 + get_Min_Squares(n  - temp)) 
    return res;
'''
assert get_Min_Squares(6) == 3
assert get_Min_Squares(2) == 2
assert get_Min_Squares(4) == 1
