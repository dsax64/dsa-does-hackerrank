import unittest
import re


def is_hackerrank_in_tweet(tweet):
    return re.match('.*hackerrank.*', tweet, re.IGNORECASE)


def solve():
    n = int(raw_input())
    count = 0
    for _ in range(0, n):
        count += 1 if is_hackerrank_in_tweet(raw_input()) else 0
    print count


class HackerRankTestCase(unittest.TestCase):
    def test_hackerrenk_in_tweet(self):
        self.assertTrue(is_hackerrank_in_tweet('I love #hackerrank'))
        self.assertTrue(is_hackerrank_in_tweet('I just scored 27 points in the Picking Cards challenge on #HackerRank'))
        self.assertTrue(is_hackerrank_in_tweet('I just signed up for summer cup @hackerrank'))
        self.assertTrue(is_hackerrank_in_tweet('interesting talk by hari, co-founder of hackerrank'))


if __name__ == '__main__':
    unittest.main()
