import unittest
import re


def is_valid_utopian_id(id):
    pattern = re.compile(r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$')
    return pattern.match(id)


def solve():
    n = int(raw_input())
    for _ in range(0, n):
        output = 'VALID' if is_valid_utopian_id(raw_input()) else 'INVALID'
        print output


class UtopianIDTestCase(unittest.TestCase):
    def test_is_valid_utopian_id(self):
        self.assertTrue(is_valid_utopian_id('abc012333ABCDEEEE'))
        self.assertTrue(is_valid_utopian_id('012333ABCDEEEE'))
        self.assertTrue(is_valid_utopian_id('01ABCDEEEE'))
        self.assertTrue(is_valid_utopian_id('01ABC'))
        self.assertFalse(is_valid_utopian_id('01BC'))
        self.assertFalse(is_valid_utopian_id('0BCD'))
        self.assertFalse(is_valid_utopian_id('0123AB'))

if __name__ == '__main__':
    unittest.main()
