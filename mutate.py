# mutation with ast/astor interface
import ast as a
import astor as ar
from IPython.utils.capture import capture_output

def str_to_ast(program_str):
    ''' renders abstract syntax tree representation of program from string representation '''
    return a.parse(program_str)

def ast_to_str(program_ast):
    ''' recovers program from abstract syntax tree representation '''
    return ar.to_source(program_ast)

def validate_ast(program_ast):
    ''' returns boolean indicating if program_ast (abstract syntax tree representation) generates code that runs '''
    try:
        with capture_output() as c:
            c = exec(ar.to_source(program_ast))
        return True
    except:
        return False

def verify_mutation(ast_a, ast_b):
    ''' returns boolean indicating disequality between abstract syntax trees by checking for differences between their string representations'''
    assert isinstance(ast_a, a.AST) and isinstance(ast_b, a.AST)
    ast_a_str = ast_to_str(ast_a)
    ast_b_str = ast_to_str(ast_b)
    return ast_a_str != ast_b_str

def count_nodes(program_ast):
    ''' counts nodes in an ast representation '''
    return len([node for node in program_ast.body])


