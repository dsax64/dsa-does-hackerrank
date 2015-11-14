import unittest


def is_valid_postal_code(postal_code):
    """no if statement is allowed"""
    try:
        within_range = 100000 < int(postal_code) < 999999
    except ValueError:
        return False

    repetative_digit_count = 0
    for i in range(0, len(postal_code) - 2):
        repetative_digit_count += int(postal_code[i] == postal_code[i + 2])
    return within_range and repetative_digit_count < 2


def solve():
    print is_valid_postal_code(raw_input())


class PostalCodeTestCase(unittest.TestCase):
    def test_is_valid_postal_code(self):
        self.assertTrue(is_valid_postal_code('523563'))
        self.assertTrue(is_valid_postal_code('123456'))
        self.assertTrue(is_valid_postal_code('121426'))
        self.assertFalse(is_valid_postal_code('552523'))
        self.assertFalse(is_valid_postal_code('110000'))
        self.assertFalse(is_valid_postal_code('303121'))

if __name__ == '__main__':
    unittest.main()
