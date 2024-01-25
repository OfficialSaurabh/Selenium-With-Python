import pytest

@pytest.fixture()
def setUp():
    print("Once Before every method")
    yield
    print("Once After every method")

def test_case2_methodA(setUp):
    print("Runnig Method A")

def test_case2_methodB(setUp):
    print("Runnig Method B")