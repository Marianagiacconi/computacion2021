import unittest


def roman_to_decimal(roman_number):
    return len(roman_number)


class TestRomanToDecimal(unittest.TestCase):

    def test_roman_I(self):
        result = roman_to_decimal('I')
        self.assertEqual(result, 1)

    def test_roman_II(self):
        result = roman_to_decimal('II')
        self.assertEqual(result, 2)

    def test_roman_II(self):
        result = roman_to_decimal('III')
        self.assertEqual(result, 3)

    def test_roman_II(self):
        result = roman_to_decimal('IV')
        self.assertEqual(result, 4)

    def test_roman_II(self):
        result = roman_to_decimal('V')
        self.assertEqual(result, 5)

    def test_roman_II(self):
        result = roman_to_decimal('VI')
        self.assertEqual(result, 6)

    def test_roman_II(self):
        result = roman_to_decimal('VII')
        self.assertEqual(result, 7)

    def test_roman_II(self):
        result = roman_to_decimal('VIII')
        self.assertEqual(result, 8)

    def test_roman_II(self):
        result = roman_to_decimal('IX')
        self.assertEqual(result, 9)

    def test_roman_II(self):
        result = roman_to_decimal('X')
        self.assertEqual(result, 10)

    def test_roman_II(self):
        result = roman_to_decimal('CC')
        self.assertEqual(result, 200)

    def test_roman_II(self):
        result = roman_to_decimal('CM')
        self.assertEqual(result, 900)

    def test_roman_II(self):
        result = roman_to_decimal('DL')
        self.assertEqual(result, 550)

if __name__ == '_main_':
    unittest.main()