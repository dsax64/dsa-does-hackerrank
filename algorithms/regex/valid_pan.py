import unittest
import re


def is_valid_pan(pan):
    return re.match('[A-Z]{5}[0-9]{4}[A-Z]', pan)


class ValidatePanTestCase(unittest.TestCase):
    def test_valid_pan(self):
        self.assertTrue(is_valid_pan('ABCDS1234Y'))

    def test_invalid_pan(self):
        self.assertFalse(is_valid_pan('ABAB12345Y'))
        self.assertFalse(is_valid_pan('avCDS1234Y'))
        self.assertFalse(is_valid_pan('1111111111'))
        self.assertFalse(is_valid_pan('AAAAAAAAAA'))
        self.assertFalse(is_valid_pan('ABCDS12342'))
        self.assertFalse(is_valid_pan(''))

if __name__ == '__main__':
    unittest.main()
