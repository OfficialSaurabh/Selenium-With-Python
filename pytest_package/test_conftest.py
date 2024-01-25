import pytest

@pytest.fixture()
def test_methodA(setUp):
    print("Runnig confest Method A")

def test_methodB(setUp):
    print("Runnig confest Method B")