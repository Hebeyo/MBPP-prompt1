"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the sum of all digits of the base to the specified power.
'''

def power_base_sum(base, power):
    result = base**power
    sum = 0
    for i in str(result):
        sum += int(i)
    return sum

'''
Standard answer: 
def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])
'''
assert power_base_sum(2,100)==115
assert power_base_sum(8,10)==37
assert power_base_sum(8,15)==62
