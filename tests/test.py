import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()