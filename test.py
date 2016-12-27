import mutate as mu
import main as m
import runner as r
import ast as a
import os
from shutil import copyfile
from shutil import copytree
from shutil import rmtree
from copy import copy, deepcopy

TEST_DIR = 'test_data/pytest_examples/'
TEST_FILES = list(map((lambda x: TEST_DIR + x), ['test_some_pass.py', 'test_all_pass.py', 'test_all_fail.py', 'test_empty']))
TEST_PROJECT = "test_data/test_project/"

def test_str_to_ast():
    valid_python = "2 + 2"
    observed = mu.str_to_ast(valid_python)
    assert isinstance(observed, a.AST)

def test_ast_to_str():
    # TODO: flaky test! we don't want to test for exact equality, but instead for same result of execution
    valid_python = "(2 + 2)"
    some_ast = a.parse(valid_python)
    observed = mu.ast_to_str(some_ast)
    assert valid_python == observed

def test_validate_ast():
    valid_python = "(2 + 2)"
    some_ast = a.parse(valid_python)
    result = mu.validate_ast(some_ast)
    assert result

def test_verify_mutation():
    program_a_str = "1 + 1"
    program_b_str = "2 + 2"
    program_a_ast = mu.str_to_ast(program_a_str)
    program_b_ast = mu.str_to_ast(program_b_str)
    assert mu.verify_mutation(program_a_ast, program_b_ast)

def test_count_nodes():
    valid_python = "2+2;3+3;x=2"
    EXPECTED_N_NODES = 3
    program_ast = a.parse(valid_python)
    observed_n_nodes = mu.count_nodes(program_ast)
    assert EXPECTED_N_NODES == observed_n_nodes

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

def test_generate_temp_filename():
    target_file = "test_data/test_project/" # TODO: abstract out file references
    assert os.path.isdir(target_file)
    result = m.generate_temp_filename(target_file)
    assert isinstance(result, str)

def test_program_as_str():
    program_file = TEST_PROJECT + "main.py"
    assert os.path.isfile(program_file)
    program_str = m.program_as_str(program_file)
    assert isinstance(program_str, str)

def test_recover_src_file():
    test_file_path = "test_data/test_project/test_file.py"
    src_file_path = "test_data/test_project/main.py"
    if os.path.isfile(test_file_path):
        os.remove(test_file_path)
    open(test_file_path, 'a').close()
    assert os.path.isfile(test_file_path)
    m.recover_src_file(src_file_path, test_file_path)
    test_file_cont_str = m.program_as_str(test_file_path)
    src_file_cont_str = m.program_as_str(src_file_path)
    os.remove(test_file_path)
    assert src_file_cont_str == test_file_cont_str

def test_overwrite_file():
    test_file_path = "test_data/test_project/test_file.py"
    if os.path.isfile(test_file_path):
        os.remove(test_file_path)
    init_content_str = "2 + 2"
    with open(test_file_path, 'a') as f:
        f.write(init_content_str)
        f.close()
    assert os.path.isfile(test_file_path)
    new_content_str = "5 + 5"
    m.overwrite_file(test_file_path, new_content_str)
    observed_content_str = m.program_as_str(test_file_path)
    os.remove(test_file_path)
    assert init_content_str != observed_content_str

def test_run_mutation_test():
    test_project_path = "test_data/test_project"
    temp_project_path = "/tmp/test_project"
    temp_src_path = "/tmp/test_project/main.py"
    temp_test_path = "/tmp/test_project/test.py"
    rel_src_path = "test_data/test_project/main.py"
    copytree(test_project_path, temp_project_path)
    result = m.run_mutation_test(temp_src_path, temp_test_path, rel_src_path)
    rmtree(temp_project_path) # TODO: clean directory
    assert isinstance(result, dict)

def test_type_in_union():
    test_union = {int, tuple, str}
    non_member_1 = mu.type_in_union(1.0, test_union)
    non_member_2 = mu.type_in_union([1, 2, 3], test_union)
    non_member_3 = mu.type_in_union(int, test_union)
    rejects_non_members =  not non_member_1 and not non_member_2 and not non_member_3
    member_1 = mu.type_in_union(1, test_union)
    member_2 = mu.type_in_union((100, "y"), test_union)
    member_3 = mu.type_in_union("xyz", test_union)
    accepts_members = member_1 and member_2 and member_3
    assert rejects_non_members and accepts_members

def test_count_constants():
    EXPECTED_NODE_COUNT = 3
    test_program = "2; \"aenima\"; True"
    test_root = a.parse(test_program)
    observed_node_count = mu.count_constants(test_root)
    assert EXPECTED_NODE_COUNT == observed_node_count

def test_substitute_value():
    test_program = "2; \"aenima\"; True"
    test_root = a.parse(test_program)
    test_nodes = [n for n in a.walk(test_root)]
    num_node = test_nodes[4]
    str_node = test_nodes[5]
    nameconstant_node = test_nodes[6]
    prior_num_value = copy(num_node.n)
    prior_str_value = copy(str_node.s)
    prior_nameconstant_value = copy(nameconstant_node.value)
    mu.substitute_value(num_node)
    mu.substitute_value(str_node)
    mu.substitute_value(nameconstant_node)
    num_passing = num_node.n != prior_num_value and isinstance(num_node.n, int)
    str_passing = str_node.s != prior_str_value and isinstance(str_node.s, str)
    nameconstant_passing = nameconstant_node.value != prior_nameconstant_value
    assert num_passing and str_passing and nameconstant_passing

def test_mutate_constants():
    test_program = "2; \"aenima\"; True"
    test_root = a.parse(test_program)
    test_root_prior = deepcopy(test_root)
    mu.mutate_constants(test_root)
    assert mu.verify_mutation(test_root, test_root_prior)
