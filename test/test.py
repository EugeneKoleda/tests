import unittest
import sys
import os

sys.path.append(os.getcwd())
from main import *


class TestNitriteSalt(unittest.TestCase):
    def test_nitrite_salt_returns_weight(self):
        self.assertEqual(nitrite_salt(1000), 10)
        self.assertEqual(nitrite_salt(1500), 15)
        self.assertEqual(nitrite_salt(800), 8)

    def test_nitrite_salt_returns_integer(self):
        self.assertIsInstance(nitrite_salt(1000), int)

    def test_nitrite_salt_receives_string_return_integer(self):
        self.assertEqual(nitrite_salt('1000'), 10)

    def test_nitrite_salt_receives_alpha_string_return_integer(self):
        self.assertEqual(nitrite_salt('adadda'), 0)

if __name__ == "__main__":
    unittest.main()
