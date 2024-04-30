"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert snake case string to camel case string.
'''

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

'''
Standard answer: 
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))
'''
assert snake_to_camel('python_program')=='PythonProgram'
assert snake_to_camel('python_language')==('PythonLanguage')
assert snake_to_camel('programming_language')==('ProgrammingLanguage')
