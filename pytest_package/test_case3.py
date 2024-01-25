'''
file name should start with test
test method name should start with test_

py.test test_mod.py # run test in module
py.test somepath #run all the test belo somepath
py.test test_module.py::test_method # Only run test_method in the test_module
-s to print statements
-v for verbose

'''

import pytest

@pytest.fixture()
def setUp():
    print("Once Before every method")
    yield
    print("Once After every method")

def test_case3_methodA(setUp):
    print("Runnig Method A of Test Case 3")

def test_case3_methodB(setUp):
    print("Runnig Method B of Test Case 3")