"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the smallest multiple of the first n numbers.
'''


def smallest_multiple(n):
    if n==1:
        return 1
    i = n
    while True:
        for a in range(1, n+1):
            if i % a != 0:
                i += n
                break
            if a == n:
                return i

'''
Standard answer: 
def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i
'''
assert smallest_multiple(13)==360360
assert smallest_multiple(2)==2
assert smallest_multiple(1)==1
