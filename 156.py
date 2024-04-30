"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert a tuple of string values to a tuple of integer values.
'''

def tuple_int_str(tuple_str):
    result = []
    for x in tuple_str:
        result.append((int(x[0]), int(x[1]))    )
    return tuple(result)


'''
Standard answer: 
def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result
'''
assert tuple_int_str((('333', '33'), ('1416', '55')))==((333, 33), (1416, 55))
assert tuple_int_str((('999', '99'), ('1000', '500')))==((999, 99), (1000, 500))
assert tuple_int_str((('666', '66'), ('1500', '555')))==((666, 66), (1500, 555))
