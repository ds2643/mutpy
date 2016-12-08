# tests accompanying main module of mutpy mutation testing tool; uses pytest as unit testing framework

import main as m
from redbaron import RedBaron

# TODO: write tests mocking occurances of each node type of red baron ast representation to test mutation function

def test_BinaryNode():
    str_repr_i= "0b10101"
    mock_program = RedBaron(string_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_BinaryOperatorNode():
    str_repr_i = "1 + 1"
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_BooleanOperatorNode():
    str_repr_i= "x and y"
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_ComparisonNode():
    str_repr_i= "42 > 30"
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_DictNode():
    str_repr_i= "{'a': 1, 'b':2, 'c': 3}"
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_IntNode():
    str_repr_i= "42"
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_ListNode():
    str_repr_i= "[1, 2, 3]"
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_SetNode():
    str_repr_i= "{1, 2, 3}"
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_StringNode():
    str_repr_i= "\"hello world\""
    mock_program = RedBaron(str_repr_i)
    mutant = m.mutate(mock_program)
    str_repr_f = m.recover_program(mutant)
    assert (str_repr_f != str_repr_i)

def test_verify_mutation():
    ast_a = RedBaron("123")
    ast_b = RedBaron("[1, 2, 3]")
    assert (m.verify_mutation(ast_a, ast_b))

def test_validate_ast():
    valid_ast = RedBaron("2 + 2 #valid python")
    assert (m.validate_ast(valid_ast))

def test_program_as_ast():
    result = program_as_ast("./data/example.py") # TODO: relative file path
    assert (isinstance(result, redbaron.redbaron.RedBaron))

def test_recover_program():
    initial_program = "2 + 2"
    transformation = RedBaron(initial_program)
    final_program = m.recover_program(transformation)
    assert (final_program == initial_program)
