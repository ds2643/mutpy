# tests accompanying main module of mutpy mutation testing tool; uses pytest as unit testing framework

import main as m
from redbaron import RedBaron

# TODO: write tests mocking occurances of each node type of red baron ast representation to test mutation function

def test_BinaryNode():
    str_repr_i= "0b10101"
    mock_program = RedBaron(string_repr_i)
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_BinaryOperatorNode():
    str_repr_i = "1 + 1"
    mock_program = RedBaron(str_repr_i)
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_BooleanOperatorNode():
    mock_program = RedBaron("x and y")
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_ComparisonNode():
    mock_program = RedBaron("42 > 30")
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_DictNode():
    mock_program = RedBaron("{'a': 1, 'b':2, 'c': 3}")
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_IntNode():
    mock_program = RedBaron("42")
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_ListNode():
    mock_program = RedBaron("[1, 2, 3]")
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_SetNode():
    mock_program = RedBaron("{1, 2, 3}")
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)

def test_StringNode():
    mock_program = RedBaron("\"hello world\"")
    str_repr_f = m.recover_program(_)
    assert(str_repr_f != str_repr_i)



