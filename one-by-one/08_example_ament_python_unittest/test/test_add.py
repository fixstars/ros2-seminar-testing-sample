import unittest
from example_ament_python_unittest.add import add


class AddTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(add(1, 2), 3)

    # def test_failure(self):
    #     self.assertEqual(add(1, 2), 4)
