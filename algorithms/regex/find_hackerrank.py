import unittest
import re


def starts_with_hackerrank(conversation):
    pattern = re.compile(r'^hackerrank.*$')
    return pattern.search(conversation)


def ends_with_hackerrank(conversation):
    pattern = re.compile(r'.*hackerrank$')
    return pattern.search(conversation)


def hackerrank_score(conversation):
    score = -1
    starts = starts_with_hackerrank(conversation)
    ends = ends_with_hackerrank(conversation)
    if starts and ends:
        score = 0
    elif ends:
        score = 2
    elif starts:
        score = 1
    return score


def solve():
    n = int(raw_input())
    for _ in range(0, n):
        print hackerrank_score(raw_input())


class HackerRankTestCase(unittest.TestCase):
    def test_starts_with_hackerrank(self):
        self.assertTrue(starts_with_hackerrank('hackerrank is an awesome place for programmers'))
        self.assertTrue(starts_with_hackerrank('hackerrank'))
        self.assertFalse(starts_with_hackerrank('i think hackerrank is a great place to hangout'))
        self.assertFalse(starts_with_hackerrank('i love hackerrank'))

    def test_ends_with_hackerrank(self):
        self.assertTrue(ends_with_hackerrank('i love hackerrank'))
        self.assertTrue(ends_with_hackerrank('hackerrank'))
        self.assertFalse(ends_with_hackerrank('i think hackerrank is a great place to hangout'))
        self.assertFalse(ends_with_hackerrank('hackerrank is an awesome place for programmers'))

    def test_hackerrank_score(self):
        self.assertEqual(2, hackerrank_score('i love hackerrank'))
        self.assertEqual(1, hackerrank_score('hackerrank is an awesome place for programmers'))
        self.assertEqual(0, hackerrank_score('hackerrank'))
        self.assertEqual(-1, hackerrank_score('i think hackerrank is a great place to hangout'))

if __name__ == '__main__':
    unittest.main()
