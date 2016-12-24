import sys
import runner as r
import tempfile
from shutil import copyfile
import os.path
import random as rnd
import mutate as m

TEMP_DIR = "/tmp/"

def generate_temp_filename(temp_dir):
    ''' generate a str filename representation that does not conflict with other file names in the temp directory '''
    possible_name = "project" + str(rnd.randint(100,10000))
    possible_path = temp_dir + possible_name
    if os.path.isfile(possible_path):
        return generate_temp_filename(temp_dir)
    else:
        return possible_name

def test_results(test_path):
    ''' dictionary of results prior to mutation '''
    return r.parse_pytest_result(test_path)

def recover_src_file(temp_src_path, rel_src_path):
    ''' restores src file to prior state'''
    assert os.path.isfile(temp_src_path)
    assert os.path.isfile(rel_src_path)
    copyfile(rel_src_path, temp_src_path)

def program_as_str(path):
    ''' returns program specified by argument as string'''
    try:
        str_repr = open(path,'r').read()
    except:
        str_repr = None
    return str_repr

def overwrite_file(file_path, program_str):
    ''' replaces previous file contents with specified string '''
    # TODO: test
    assert os.path.isfile(file_path)
    with open(file_path, 'w') as f:
        f.write(program_str)
        f.close()

def run_mutation_test(temp_src_path, temp_test_path, rel_src_path):
    ''' collect dictionary of results from mutating src '''
    # TODO: test
    assert os.path.isfile(temp_src_path)
    assert os.path.isfile(temp_test_path)
    src_str = program_as_str(temp_src_path)
    src_ast = m.str_to_ast(src_str)
    mutant_ast = m.false_mutation(src_ast) # TODO: substitute for real mutation alg
    assert m.validate_ast(mutant_ast)
    mutant_str = m.ast_to_str(mutant_ast)
    overwrite_file(temp_src_path, mutant_str)
    mutant_test_results = test_results(temp_test_path)
    recover_src_file(temp_src_path, rel_src_path)
    return mutant_test_results

def run_n_mutations(n):
    ''' return result of n mutation test trials '''
    pass

if __name__ == "__main__":
    # TODO: support multiple src and tests files with argparse module
    project_path = sys.argv[1]
    rel_src_path = sys.argv[2]
    rel_test_path = sys.argv[3]
    iterations = sys.argv[4]
    temp_file_name = generate_temp_filename(TEMP_DIR)
    assert isinstance(project_path, str) and os.path.isfile(project_path)
    temp_project_path = TEMP_DIR + temp_file_name
    temp_test_path = temp_project_path + "/" + rel_test_path
    temp_src_path = temp_project_path + "/" + rel_src_path

    # prepare copy of project for munipulation
    copyfile(project_path, temp_project_path)
    assert os.path.isfile(temp_test_path)

    init_test_results = test_results(temp_test_path)
    run_mutation_test(temp)
    # TODO: print results; later add csv log support
