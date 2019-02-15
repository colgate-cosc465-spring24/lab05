#!/usr/bin/python3

import ipaddress
import ipsubnet
import unittest

class TestIsAdjacent(unittest.TestCase):
    def test_yes_same_prefixlen(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.0.0.0/8'))
        self.assertEqual(actual, True)

    def test_yes_diff_prefixlen(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.0.0.0/16'))
        self.assertEqual(actual, True)

    def test_yes_address(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('10.0.0.0/32'),
                ipaddress.IPv4Network('10.0.0.1/32'))
        self.assertEqual(actual, True)

    def test_yes_inverted(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('11.0.0.0/8'),
                ipaddress.IPv4Network('10.0.0.0/8'))
        self.assertEqual(actual, True)

    def test_no_same_prefixlen(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('12.0.0.0/8'))
        self.assertEqual(actual, False)

    def test_no_diff_prefixlen(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.1.0.0/16'))
        self.assertEqual(actual, False)

    def test_no_address(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('10.0.0.0/32'),
                ipaddress.IPv4Network('11.0.0.0/32'))
        self.assertEqual(actual, False)

    def test_no_inverted(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('12.0.0.0/8'),
                ipaddress.IPv4Network('10.0.0.0/8'))
        self.assertEqual(actual, False)


if __name__ == '__main__':
    unittest.main()
        
