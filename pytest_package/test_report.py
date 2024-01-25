import pytest
from pytest_package.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("OneTimesetUp", "setUp")
class TestReport():
    @pytest.fixture(autouse=True)
    def classSetup(self, OneTimesetUp):
        self.abc = SomeClassToTest(self.value)
    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("Running method B")