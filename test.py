# tests accompanying main module of mutpy mutation testing tool; uses pytest as unit testing framework

# TODO: write tests mocking occurances of each node type of red baron ast representation to test mutation function

import main as m
from redbaron import RedBaron
import runner as r

TEST_DIR = 'test_data/pytest_examples/'
TEST_FILES = list(map((lambda x: TEST_DIR + x), ['test_some_pass.py', 'test_all_pass.py', 'test_all_fail.py', 'test_empty']))

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
    result = m.program_as_ast("./data/example.py") # TODO: relative file path
    assert (isinstance(result, redbaron.redbaron.RedBaron))

def test_recover_program():
    initial_program = "2 + 2"
    transformation = RedBaron(initial_program)
    final_program = m.recover_program(transformation)
    assert (final_program == initial_program)

def test_pytest_result():
    ''' result of capturing the result of running a test in code is a string '''
    test_file = TEST_FILES[0]
    observed_result = r.pytest_result(test_file)
    assert isinstance(observed_result, str)

def test_find_total():
    ''' successfully parse result of running tests to yield int representation of total tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = r.pytest_result(test_file)
    EXPECTED_TOTAL = 2
    observed_total = r.find_total(pytest_result)
    assert EXPECTED_TOTAL == observed_total

def test_find_passed():
    ''' successfully parse result of running tests to yield int representation of passed tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = r.pytest_result(test_file)
    EXPECTED_PASSED = 1
    observed_passed = r.find_passed(pytest_result)
    assert EXPECTED_PASSED == observed_passed

def test_find_failed():
    ''' successfully parse result of running tests to yield int representation of failed tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = r.pytest_result(test_file)
    EXPECTED_FAILED = 1
    observed_failed = r.find_failed(pytest_result)
    assert EXPECTED_FAILED == observed_failed

def test_find_time():
    ''' successfully parse result of running tests to yield int representation of passed tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = r.pytest_result(test_file)
    observed_time = r.find_time(pytest_result)
    assert isinstance(observed_time, float)

def test_parse_pytest_result_mixed():
    ''' end-to-end test of parsing test result to dict for test file of mixed results '''
    test_file = TEST_FILES[0]
    EXPECTED_PASSED = 1
    EXPECTED_FAILED = 1
    EXPECTED_TOTAL = 2
    actual = r.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL

def test_parse_pytest_result_passing():
    ''' end-to-end test of parsing test result to dict for test file of uniform passing results '''
    test_file = TEST_FILES[1]
    EXPECTED_PASSED = 2
    EXPECTED_FAILED = None
    EXPECTED_TOTAL = 2
    actual = r.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL

def test_parse_pytest_result_failing():
    ''' end-to-end test of parsing test result to dict for test file of uniform failing results '''
    test_file = TEST_FILES[2]
    EXPECTED_PASSED = None
    EXPECTED_FAILED = 2
    EXPECTED_TOTAL = 2
    actual = r.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL

def test_parse_pytest_result_empty():
    ''' end-to-end test of parsing test result to dict for an empty test file '''
    test_file = TEST_FILES[3]
    EXPECTED_PASSED = None
    EXPECTED_FAILED = None
    EXPECTED_TOTAL = None
    actual = r.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL
