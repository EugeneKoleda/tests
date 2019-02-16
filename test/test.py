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


class TestSalt(unittest.TestCase):
    def test_salt_returns_weight(self):
        self.assertEqual(salt(1000), 15)
        self.assertEqual(salt(1500), 22)
        self.assertEqual(salt(800), 12)

    def test_salt_returns_integer(self):
        self.assertIsInstance(salt(1000), int)

    def test_salt_receives_string_return_integer(self):
        self.assertEqual(salt('1000'), 15)

    def test_salt_receives_alpha_string_return_integer(self):
        self.assertEqual(salt('adadda'), 0)


class TestSpices(unittest.TestCase):
    def test_spices_returns_weight(self):
        self.assertEqual(spices(1000), 0.5)
        self.assertEqual(spices(1500), 0.75)
        self.assertEqual(spices(800), 0.4)

    def test_spices_returns_integer(self):
        self.assertIsInstance(spices(1000), float)

    def test_spices_receives_string_return_integer(self):
        self.assertEqual(spices('1000'), 0.5)

    def test_spices_receives_alpha_string_return_integer(self):
        self.assertEqual(spices('adadda'), 0)


class TestMonosaccharides(unittest.TestCase):
    def test_monosaccharides_returns_weight(self):
        self.assertEqual(monosaccharides(1000), 5)
        self.assertEqual(monosaccharides(1500), 7)
        self.assertEqual(monosaccharides(800), 4)

    def test_monosaccharides_returns_integer(self):
        self.assertIsInstance(monosaccharides(1000), int)

    def test_monosaccharides_receives_string_return_integer(self):
        self.assertEqual(monosaccharides('1000'), 5)

    def test_monosaccharides_receives_alpha_string_return_integer(self):
        self.assertEqual(monosaccharides('adadda'), 0)


class TestDays(unittest.TestCase):
    def test_days_returns_weight(self):
        self.assertEqual(days(1000), 2)
        self.assertEqual(days(1500), 3)
        self.assertEqual(days(800), 1)

    def test_days_returns_integer(self):
        self.assertIsInstance(days(1000), int)

    def test_days_receives_string_return_integer(self):
        self.assertEqual(days('1000'), 2)

    def test_days_receives_alpha_string_return_integer(self):
        self.assertEqual(days('adadda'), 0)


if __name__ == "__main__":
    unittest.main()
