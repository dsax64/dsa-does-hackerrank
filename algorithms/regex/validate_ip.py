import unittest
import re


def is_valid_ip4(ip):
    pattern = re.compile(r'((^|\.)([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){4}$')
    return pattern.match(ip)


def is_valid_ip6(ip):
    pattern = re.compile(r'((^|:)([0-9a-f]{1,4})){8}$')
    return pattern.match(ip)


def solve():
    n = int(raw_input())
    for _ in range(0, n):
        output = 'Neither'
        ip = raw_input()
        if is_valid_ip4(ip):
            output = 'IPv4'
        elif is_valid_ip6(ip):
            output = 'IPv6'
        print output


class IpAddressValidationTestCase(unittest.TestCase):
    def test_is_valid_ip4(self):
        self.assertTrue(is_valid_ip4('121.18.19.20'))
        self.assertTrue(is_valid_ip4('255.255.255.255'))
        self.assertTrue(is_valid_ip4('0.0.0.0'))
        self.assertTrue(is_valid_ip4('22.2.113.61'))
        self.assertTrue(is_valid_ip4('22.2.113.162'))
        self.assertTrue(is_valid_ip4('255.2.111.63'))
        self.assertTrue(is_valid_ip4('253.2.111.69'))

        self.assertFalse(is_valid_ip4('00.0.0.0'))
        self.assertFalse(is_valid_ip4('256.0.0.0'))
        self.assertFalse(is_valid_ip4('255 0.0.0'))

    def test_is_valid_ip6(self):
        self.assertTrue(is_valid_ip6('2001:0db8:0000:0000:0000:ff00:0042:8329'))
        self.assertTrue(is_valid_ip6('2001:0db8:0:0000:0000:5:0042:8329'))
        self.assertFalse(is_valid_ip6('This line has junk text.This line has junk text.  '))
        self.assertFalse(is_valid_ip6('1050:10:0:0:15:600:300c:326k'))
        self.assertFalse(is_valid_ip6('1050:10:0:0:15:600:300c:326g'))
        self.assertFalse(is_valid_ip6('1050:10:0:0:15:600:300c:326h'))
        self.assertFalse(is_valid_ip6('1050:10:0:0:15:600:300c:326i'))


if __name__ == '__main__':
    unittest.main()
    # solve()
