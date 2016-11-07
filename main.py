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

def count_ast_nodes_helper(node):
    ''' count nodes in the AST '''
    # TODO:  fix
    node_count = 1
    try:
        for child in node:
            node_count += count_ast_nodes_helper(child)
        return node_count
    except:
        return 0

# TODO: substitution function node types: https://github.com/PyCQA/redbaron/blob/497a55f51a1902f67b30519c126469e60b4f569f/docs/nodes_reference.rst

def mutate(ast):
    total_nodes = count_ast_nodes(ast)
    transformations = dict()
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

