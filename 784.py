"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the product of first even and odd number of a given list.
'''

def mul_even_odd(list1):
    even = False
    odd = False
    for i in list1:
        if i%2==0 and even==False:
            even = True
            even_num = i
        elif i%2!=0 and odd==False:
            odd = True
            odd_num = i
    return even_num*odd_num

'''
Standard answer: 
def mul_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even*first_odd)
'''
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
assert mul_even_odd([1,5,7,9,10])==10
