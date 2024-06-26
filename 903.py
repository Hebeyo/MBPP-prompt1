"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the total unset bits from 1 to n.
'''

def count_Unset_Bits(n) :  
    cnt = 0;  
    for i in range(1,n + 1) : 
        temp = i;  
        while (temp) :  
            if (temp % 2 == 0) : 
                cnt += 1;  
            temp = temp // 2;  
    return cnt;

'''
Standard answer: 
def count_Unset_Bits(n) :  
    cnt = 0;  
    for i in range(1,n + 1) : 
        temp = i;  
        while (temp) :  
            if (temp % 2 == 0) : 
                cnt += 1;  
            temp = temp // 2;  
    return cnt;  
'''
assert count_Unset_Bits(2) == 1
assert count_Unset_Bits(5) == 4
assert count_Unset_Bits(14) == 17
