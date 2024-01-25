import unittest

class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("#" * 20)
        print("I will run once before all tests")
        print("#" * 20)
    def setUp(self):
        print("I will run once before each test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run once after each test")

    @classmethod
    def tearDownClass(cls):
        print("#" * 20)
        print("I will run once after all tests")
        print("#" * 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)
