from IPython.utils.capture import capture_output
import re

def pytest_result(test_path):
    ''' runs specified pytest test-file, returns captured result as string '''
    try:
        import pytest
        with capture_output() as c:
            pytest.main([test_path])
        return c.stdout
    except ImportError:
        print("failed to import pytest")
        return None

def find_total(pytest_result):
    ''' given string representation of pytest result finds total number of cases '''
    try:
        raw_str = re.compile("collected\s\d+\sitems").findall(pytest_result)[0]
        total = int(re.compile("\d+").findall(raw_str)[0])
    except IndexError:
        total = None
    return total

def find_passed(pytest_result):
    ''' given string representation of pytest result finds number of passed cases '''
    try:
        raw_str = re.compile("\d\spassed").findall(pytest_result)[0]
        passed = int(re.compile("\d+").findall(raw_str)[0])
    except IndexError:
        passed = None
    return passed

def find_failed(pytest_result):
    ''' given string representation of pytest result finds number of failed cases '''
    try:
        raw_str = re.compile("\d\sfailed").findall(pytest_result)[0]
        failed = int(re.compile("\d+").findall(raw_str)[0])
    except IndexError:
        failed = None
    return failed

def find_time(pytest_result):
    ''' given string representation of pytest result finds time to completion '''
    try:
        raw_str = re.compile("\d+\.\d\d\sseconds").findall(pytest_result)[0]
        time_elapsed = float(re.compile("\d+\.\d\d").findall(raw_str)[0])
    except IndexError:
        time_elapsed = None
    return float(time_elapsed)

def parse_pytest_result(test_path):
    ''' parses string result of calling pytest '''
    test_outcome = pytest_result(test_path)
    result = dict()
    result["total"] = find_total(test_outcome)
    result["passed"] = find_passed(test_outcome)
    result["failed"] = find_failed(test_outcome)
    result["time"] = find_time(test_outcome)
    return result
