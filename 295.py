"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to return the sum of all divisors of a number.
'''
def sum_div(number):
    s = 1
    for i in range(2,number):
        if number%i==0:
            s+=i
    return s

'''
Standard answer: 
def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
'''
assert sum_div(8)==7
assert sum_div(12)==16
assert sum_div(7)==1
