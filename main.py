'''
mutation testing in python
'''
from redbaron import RedBaron

def program_as_ast(path):
    ''' returns program (specified by path) as Python abstract syntax tree'''
    # retrofit with try/except
    str_repr = open(path,'r').read()
    return RedBaron(str_repr)

def recover_program(ast):
    ''' transform ast to programmatic string '''
    str_repr = ast.dumps()
    return str_repr


def valid_ast(ast):
    ''' returns boolean indicating if program runs'''
    try:
        exec(ast.dumps())
        return True
    except:
        return False
