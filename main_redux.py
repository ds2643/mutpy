import sys
import runner as r
import tempfile
from shutil import copyfile
import os.path
import random as rnd

TEMP_DIR = "/tmp/"

def generate_temp_filename(temp_dir):
    ''' generate a str filename representation that does not conflict with other file names in the temp directory '''
    possible_name = "project" + str(rnd.randint(100,10000))
    possible_path = temp_dir + possible_name
    if os.path.isfile(possible_path):
        return generate_temp_filename(temp_dir)
    else:
        return possible_name

def seed_test_results(test_path):
    ''' dictionary of results prior to mutation '''
    return r.parse_pytest_result(test_path)

def recover_src_file(temp_src_path, rel_src_path):
    ''' restores src file to prior state'''
    assert os.path.isfile(temp_src_path)
    assert os.path.isfile(rel_src_path)
    copyfile(rel_src_path, temp_src_path)


if __name__ == "__main__":
    project_path = sys.argv[1]
    # TODO: support multiple src and tests files with argparse module
    rel_src_path = sys.argv[2]
    rel_test_path = sys.argv[3]
    temp_file_name = generate_temp_filename(TEMP_DIR)

    assert isinstance(project_path, str) and os.path.isfile(project_path)
    temp_project_path = TEMP_DIR + temp_file_name
    copyfile(project_path, temp_project_path)
    temp_test_path = temp_project_path + "/" + rel_test_path
    assert os.path.isfile(temp_test_path)
    temp_src_path = temp_project_path + "/" + rel_src_path
    assert os.path.isfile(temp_src_path)

    # ...
    init_test_results = seed_test_results(temp_test_path)
    # TODO: transform to loop

