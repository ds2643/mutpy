'''
mutation testing in python
'''
from redbaron import RedBaron
import redbaron.nodes as n

def program_as_ast(path):
    ''' returns program (specified by path) as Python abstract syntax tree'''
    # retrofit with try/except
    str_repr = open(path,'r').read()
    return RedBaron(str_repr)

def recover_program(ast):
    ''' transform ast to programmatic string '''
    str_repr = ast.dumps()
    return str_repr

def validate_ast(ast):
    ''' returns boolean indicating if program runs'''
    try:
        exec(ast.dumps()) # TODO: redirect outpurt
        return True
    except:
        return False

def safety_validation(ast):
    ''' ensures program has no harmful side effects '''
    return None

#TODO for now, hard code mutations into walk


def count_ast_nodes(node):
    node_count = 1
    return count_ast_nodes_helper(node)

def count_ast_nodes_helper(node):
    ''' count nodes in the AST '''
    try:
        for child in node:
            node_count += count_ast_nodes_helper(child)
        return node_count
    except:
        return 0

def walk_ast(node):
    ''' given the (root) node of an abstract syntax tree, walk the tree conditionally based on node class... ripe for substitution appliction: credit to andrea orro and james katz'''
    try:
        if isinstance(node, n.AssignmentNode):
            walk_ast(node.value)
        elif isinstance(node, n.DefNode):
            walk_ast(node.value)
        elif isinstance(node, n.NameNode):
            pass
        elif isinstance(node, n.ReturnNode):
            walk_ast(node.value)
        elif isinstance(node, n.AssociativeParenthesisNode):
            walk_ast(node.value)
        elif isinstance(node, n.BinaryOperatorNode):
            walk_ast(node.first)
            walk_ast(node.second)
        else:
            for child in node:
                walk_ast(child)
    except TypeError:
        return None

if __name__ == "__main__":
    ast = program_as_ast(argv[1])
    if validate_ast(ast):
        print(0)

