import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_not_pass(self):
        self.assertFalse(False)


unittest.main()
