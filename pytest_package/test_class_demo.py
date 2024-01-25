import pytest
from pytest_package.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("OneTimesetUp", "setUp")
class TestClass1():
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)
    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")