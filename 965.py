"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert camel case string to snake case string.
'''

def camel_to_snake(text):
    # import re
    # str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    # return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
    res = ''.join(['_'+i.lower() if i.isupper() else i for i in text]).lstrip('_')
    return res

'''
Standard answer: 
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
'''
assert camel_to_snake('PythonProgram')==('python_program')
assert camel_to_snake('pythonLanguage')==('python_language')
assert camel_to_snake('ProgrammingLanguage')==('programming_language')
