import random as r
from redbaron import RedBaron
import redbaron.nodes as n
import ast # used for count_ast_nodes

# entry/exit

def program_as_ast(program_str):
    ''' modified function returns program string as redbaron ast object'''
    return RedBaron(str_repr)

def recover_program(ast):
    ''' transform ast to programmatic string '''
    str_repr = ast.dumps()
    return str_repr

def validate_ast(ast):
    ''' returns boolean indicating if program runs'''
    try:
        from IPython.utils.capture import capture_output
        with capture_output() as c:
            exec(ast.dumps()) # TODO: redirect output
        return True
    except:
        return False

def verify_mutation(ast_a, ast_b):
    ''' returns boolean indicating if mutation succeeded in morphing genotype '''
    return ast_a.dump() != ast_b.dump()

# TODO: verify behavior of preprocessing

class NodeCounter(ast.NodeVisitor):
    ''' supports count_ast_nodes() '''
    def __init__(self):
        self.counter = 1
    def generic_visit( self, node ):
        ''' override default generic_visit '''
        self.counter += 1
    def count_nodes(self, ast):
        self.visit(ast) # begin crawling ast
        return self.counter

def count_ast_nodes(ast_alt):
    ''' counts nodes in ast given ast module representation of program '''
    return NodeCounter().generic_visit(alt_ast)

# TODO: refactor transform

TRANSFORMATIONS = {
            "BinaryNode": lambda x: x,
            "BinaryOperatorNode": lambda x: x,
            "BooleanOperatorNode": lambda x: x,
            "ComparisonNode": lambda x: x,
            "DictNode": lambda x: x,
            "IntNode": lambda x: x,
            "ListNode": lambda x: x,
            "SetNode": lambda x: x,
            "StringNode": lambda x: x}

def random_mutation(node, tranformations, p_mutation):
    ''' apply type-appropriate mutation to node with specified probability'''
    assert 0 < p_mutation < 1, ""
    if (r.random() <= p_mutation):
        node_type = type(node)
        transformation_f = transformations[node_type]
        return transformation_f(node)
    else:
        return node

def mutate_ast(ast, no_nodes, trans = TRANSFORMATIONS):
    ''' returns mutant version of programmatic ast given redbaron representation and number of nodes '''
    ast_copy = ast.copy() # single node copy or recursive copy?
    total_nodes = no_nodes
    p_tranformation = 1/total_nodes
    return random_mutation(ast_copy, tran, p_mutation)


