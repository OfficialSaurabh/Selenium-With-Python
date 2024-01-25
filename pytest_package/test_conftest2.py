import pytest

@pytest.fixture()
def test_methodA(OneTimesetUp, setUp):
    print("Runnig confest Method A")
def test_methodB(OneTimesetUp, setUp ):
    print("Runnig confest Method B")

