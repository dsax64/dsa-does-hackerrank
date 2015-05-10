import unittest
import re


def is_valid_lat_long(lat_long_pair):
    pattern = re.compile(r'^\([\+-]?(([0-9]|[1-8][0-9])(\.[0-9]+)*|90(\.0+)?), ([\+-])?(([0-9]|[1-9][0-9]|1[0-7][0-9])(\.[0-9]*)?|180(\.0+)?)\)$')
    return pattern.match(lat_long_pair)


def solve():
    n = int(raw_input())
    for _ in range(0, n):
        output = 'Valid' if is_valid_lat_long(raw_input()) else 'Invalid'
        print output


class ValidatePanTestCase(unittest.TestCase):
    def test_valid_pan(self):
        self.assertTrue(is_valid_lat_long('(75, 180)'))
        self.assertTrue(is_valid_lat_long('(+90.0, -147.45)'))
        self.assertTrue(is_valid_lat_long('(77.11112223331, 149.99999999)'))
        self.assertTrue(is_valid_lat_long('(-90.00000, -180.0000)'))
        self.assertTrue(is_valid_lat_long('(+90, +180)'))
        self.assertTrue(is_valid_lat_long('(90, 180)'))

    def test_invalid_pan(self):
        self.assertFalse(is_valid_lat_long('(-090.00000, -180.0000)'))
        self.assertFalse(is_valid_lat_long('(75, 280)'))
        self.assertFalse(is_valid_lat_long('(+190.0, -147.45)'))
        self.assertFalse(is_valid_lat_long('(77.11112223331, 249.99999999)'))
        self.assertFalse(is_valid_lat_long('(+90, +180.2)'))
        self.assertFalse(is_valid_lat_long('(90., 180.)'))


if __name__ == '__main__':
    unittest.main()
