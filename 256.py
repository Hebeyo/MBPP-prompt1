"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the number of prime numbers less than a given non-negative number.
'''

def count_Primes_nums(n):
    count = 0
    for num in range(2, n):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1
    return count

'''
Standard answer: 
def count_Primes_nums(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
'''
assert count_Primes_nums(5) == 2
assert count_Primes_nums(10) == 4
assert count_Primes_nums(100) == 25
