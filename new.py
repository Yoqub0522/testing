import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        print("Test oldidan ishga tushdi")

    def tearDown(self):
        print("Testdan keyin ishga tushdi")

    def test_example(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()