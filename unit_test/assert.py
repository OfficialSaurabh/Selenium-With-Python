# https://docs.python.org/3/library/unittest.html#unittest.TestCase

import unittest

class AssertDemo(unittest.TestCase):
    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false")

    def test_assertequal(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, "a is not equal to b")

if __name__ == "__main__":
    unittest.main(verbosity=2)
