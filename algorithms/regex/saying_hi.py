import unittest
import re


def saying_hi(id):
    pattern = re.compile(r'^hi [^d].*$', re.IGNORECASE)
    return pattern.match(id)


def solve():
    n = int(raw_input())
    for _ in range(0, n):
        output = 'VALID' if saying_hi(raw_input()) else 'INVALID'
        print output


class UtopianIDTestCase(unittest.TestCase):
    def test_is_valid_utopian_id(self):
        self.assertTrue(saying_hi('Hi Alex how are you doing'))
        self.assertFalse(saying_hi('hI dave how are you doing'))
        self.assertFalse(saying_hi('Good by Alex'))
        self.assertFalse(saying_hi('hidden agenda'))
        self.assertFalse(saying_hi('Alex greeted Martha by saying Hi Martha'))

if __name__ == '__main__':
    unittest.main()
