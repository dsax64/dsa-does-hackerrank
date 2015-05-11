import unittest
import re


def is_valid_language(id):
    pattern = re.compile(r'\d{5,6} (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$', re.IGNORECASE)
    return pattern.match(id)


def solve():
    n = int(raw_input())
    for _ in range(0, n):
        output = 'VALID' if is_valid_language(raw_input()) else 'INVALID'
        print output


class HackerRankLanguagesTestCase(unittest.TestCase):
    def test_is_valid_language(self):
        self.assertTrue(is_valid_language('11011 LUA'))
        self.assertTrue(is_valid_language('11022 BRAINFUCK'))
        self.assertFalse(is_valid_language('11044 X'))

if __name__ == '__main__':
    unittest.main()
