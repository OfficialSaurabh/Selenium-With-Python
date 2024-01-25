import pytest

@pytest.fixture()
def setUp():
    print("Once Before every thing")
def test_case1_methodA(setUp):
    print("test_methodA")

def test_case1_methodB(setUp):
    print("test_methodB")