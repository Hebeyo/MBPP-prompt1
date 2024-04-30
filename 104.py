"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to sort each sublist of strings in a given list of lists using lambda function.
'''

def sort_sublists(input_list):
    result = []
    for x in input_list:
        result.append(sorted(x, key = lambda x:x[0]))
    return result



'''
Standard answer: 
def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result
'''
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]
