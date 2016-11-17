'''
mutation testing in python
'''
import sys
import random as r
from redbaron import RedBaron
import redbaron.nodes as n
import ast # used for count_ast_nodes

def program_as_ast(path):
    ''' returns program (specified by path) as Python abstract syntax tree (Redbaron)'''
    # retrofit with try/except
    str_repr = open(path,'r').read()
    return RedBaron(str_repr)

def program_as_ast_alt(path):
    ''' returns program (specified by path) as Python abstract syntax tree (AST module) '''
    str_repr = open(path,'r').read()
    ast = ast.parse(str_repr)

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

# TODO: substitution function node types: https://github.com/PyCQA/redbaron/blob/497a55f51a1902f67b30519c126469e60b4f569f/docs/nodes_reference.rst

def random_mutation(node, tranformations, p_mutation):
    ''' apply type-appropriate mutation to node with specified probability'''
    assert 0 < p_mutation < 1, ""
    if (r.random() <= p_mutation):
        node_type = type(node)
        transformation_f = transformations[node_type]
        return transformation_f(node)
    else:
        return node

def verify_mutation(ast_a, ast_b):
    ''' returns boolean indicating if mutation succeeded in morphing genotype '''
    return ast_a.dump() != ast_b.dump()

def mutate_ast(ast, no_nodes):
    ''' returns mutant version of programmatic ast given redbaron representation and number of nodes '''
    ast_copy = ast.copy() # single node copy or recursive copy?
    total_nodes = no_nodes
    p_tranformation = 1/total_nodes # set probability of transforming a node as a function of total number of nodes
    transformations = dict() # tranformations as a function of node type
    transformations.update({
            AssertNode: lambda x: x,
            AssignmentNode: lambda x: x,
            AssociativeParenthesisNode: lambda x: x,
            AtomtrailersNode: lambda x: x,
            BinaryNode: lambda x: x,
            BinaryOperatorNode: lambda x: x,
            BooleanOperatorNode: lambda x: x,
            CallNode: lambda x: x,
            CallArgumentNode: lambda x: x,
            ClassNode: lambda x: x,
            CommaNode: lambda x: x,
            ComparisonNode: lambda x: x,
            ComprehensionIfNode: lambda x: x,
            ComprehensionLoopNode: lambda x: x,
            DecoratorNode: lambda x: x,
            DefArgumentNode: lambda x: x,
            DelNode: lambda x: x,
            DictArgumentNode: lambda x: x,
            DictNode: lambda x: x,
            DictComprehensionNode: lambda x: x,
            DottedAsNameNode: lambda x: x,
            DotNode: lambda x: x,
            ElifNode: lambda x: x,
            ElseNode: lambda x: x,
            EndlNode: lambda x: x,
            ExceptNode: lambda x: x,
            ExecNode: lambda x: x,
            FinallyNode: lambda x: x,
            ForNode: lambda x: x,
            FromImportNode: lambda x: x,
            FuncdefNode: lambda x: x,
            GeneratorComprehensionNode: lambda x: x,
            GetitemNode: lambda x: x,
            GlobalNode: lambda x: x,
            IfNode: lambda x: x,
            IfelseblockNode: lambda x: x,
            ImportNode: lambda x: x,
            IntNode: lambda x: x,
            LambdaNode: lambda x: x,
            ListArgumentNode: lambda x: x,
            ListComprehensionNode: lambda x: x,
            ListNode: lambda x: x,
            NameAsNameNode: lambda x: x,
            PrintNode: lambda x: x,
            RaiseNode: lambda x: x,
            ReprNode: lambda x: x,
            ReturnNode: lambda x: x,
            SetNode: lambda x: x,
            SetComprehensionNode: lambda x: x,
            SliceNode: lambda x: x,
            SpaceNode: lambda x: x,
            StringChainNode: lambda x: x,
            TernaryOperatorNode: lambda x: x,
            TryNode: lambda x: x,
            UnitaryOperatorNode: lambda x: x,
            YieldNode: lambda x: x,
            YieldAtomNode: lambda x: x,
            WhileNode: lambda x: x,
            WithContextItemNode: lambda x: x,
            WithNode: lambda x: x})
    random_mutation(ast_copy, tranformations, p_mutation)

if __name__ == "__main__":
    ast = program_as_ast(sys.argv[1])
    if validate_ast(ast):
        print(0)
