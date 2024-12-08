import unittest

class TestApp(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_another_example(self):
        self.assertTrue('hello'.isupper() is False)

if __name__ == '__main__':
    unittest.main()
