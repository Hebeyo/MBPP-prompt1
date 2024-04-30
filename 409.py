"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the minimum product from the pairs of tuples within a given list.
'''

def min_product_tuple(list1):
    min_product = abs(list1[0][0] * list1[0][1])
    for x, y in list1:
        if abs(x*y) < min_product:
            min_product = abs(x*y)
    return min_product

'''
Standard answer: 
def min_product_tuple(list1):
    result_min = min([abs(x * y) for x, y in list1] )
    return result_min
'''
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100
