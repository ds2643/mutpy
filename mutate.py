import ast as a
import astor as ar
from IPython.utils.capture import capture_output
from copy import deepcopy
import random as r
import sys
import string as st

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

def false_mutation(program_ast):
    ''' mutation placeholder for development for imperative shell that doesn't alter the ast '''
    # TODO: replace with real mutation function
    mutant_ast = program_ast
    return mutant_ast

def type_in_union(x, u):
    ''' returns true if type of x included in the union of types u '''
    assert isinstance(u, set)
    for t in u:
        if isinstance(x, t):
            return True
    return False

def count_constants(root):
    ''' counts instances of leaf nodes with constant values in abstract syntax tree grounded by root '''
    constant_node_types = {a.Num, a.Str, a.Bytes, a.NameConstant}
    nodes = [node for node in a.walk(root)]
    constant_nodes = list(filter(lambda x: type_in_union(x, constant_node_types), nodes))
    return len(constant_nodes)

def substitute_value(node):
    ''' impure function that takes a constant node and substitudes its value for one of the same type '''
    if isinstance(node, a.Num):
        node.n = r.randrange(0, sys.maxsize)
    elif isinstance(node, a.Str):
        l = len(node.s)
        rand_str = ''.join(r.choice(st.ascii_uppercase + st.digits) for _ in range(l))
        node.s = rand_str
    # TODO: add support for random byte generation
    #elif isinstance(node, a.Bytes):
    #    return None
    elif isinstance(node, a.NameConstant):
        if node.value:
            node.value = False
        elif not node.value:
            node.value = True
        else:
            node.value = r.random() >= 0.5

def mutate_constants(root):
    # TODO: test
    ''' mutate a random constant in the abstract syntax tree '''
    root_copy = deepcopy(root)
    n_constants = count_constants(root)
    constant_node_types = {a.Num, a.Str, a.Bytes, a.NameConstant}
    assert count_constants(root) == count_constants(root) # TODO: development check, delete post-confirmation
    p_change = 1/n_constants # probability of change
    for node in a.walk(root):
        if type_in_union(node, constant_node_types) and r.random() <= p_change:
            substitute_value(node) # no return value, change in place to accomodate for different methods associated with different node types
    if n_constants > 0 and not verify_mutation(root, root_copy):
        mutate_constants(root) # recur on failure if the ast has constant values
    return root

