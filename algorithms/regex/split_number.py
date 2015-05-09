import unittest
import re

OUTPUT_FORMAT = 'CountryCode={country_code},LocalAreaCode={local_code},Number={number}'


def split_number(number):
    pattern = re.compile(r'^(\d{1,3})[ -](\d{1,3})[ -](\d{4,10})$')
    return pattern.search(number).groups()


def solve():
    n = int(raw_input())
    for _ in range(0, n):
        matched_numbers = split_number(raw_input())
        print OUTPUT_FORMAT.format(country_code=matched_numbers[0], local_code=matched_numbers[1], number=matched_numbers[2])


class SplitNumberTestCase(unittest.TestCase):
    def test_split_number(self):
        self.assertEqual(('1', '877', '2638277'), split_number('1 877 2638277'))
        self.assertEqual(('91', '011', '23413627'), split_number('91-011-23413627'))


solve()

if __name__ == '__main__':
    unittest.main()
