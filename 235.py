"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to set all even bits of a given number.
'''

def even_bit_set_number(n): 
    count = 0;res = 0;temp = n 
    while(temp > 0): 
        if (count % 2 == 1): 
            res |= (1 << count)
        count+=1
        temp >>= 1
    return (n | res)


'''
Standard answer: 
def even_bit_set_number(n): 
    count = 0;res = 0;temp = n 
    while(temp > 0): 
        if (count % 2 == 1): 
            res |= (1 << count)
        count+=1
        temp >>= 1
    return (n | res) 
'''
assert even_bit_set_number(10) == 10
assert even_bit_set_number(20) == 30
assert even_bit_set_number(30) == 30
