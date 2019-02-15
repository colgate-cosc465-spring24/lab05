#!/usr/bin/python3

import ipaddress
import ipsubnet
import unittest

class TestIsSubnet(unittest.TestCase):
    def test_yes_same_prefix(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('10.0.0.0/16'))
        self.assertEqual(actual, True)

    def test_yes_diff_prefix(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('10.128.0.0/16'))
        self.assertEqual(actual, True)

    def test_yes_address(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('10.11.12.13/32'))
        self.assertEqual(actual, True)

    def test_no_same_prefixlen(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.0.0.0/8'))
        self.assertEqual(actual, False)

    def test_no_diff_prefixlen(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.12.0.0/16'))
        self.assertEqual(actual, False)

    def test_no_address(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.12.13.14/32'))
        self.assertEqual(actual, False)

    def test_no_inverted(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('10.0.0.0/16'),
                ipaddress.IPv4Network('10.0.0.0/8'))
        self.assertEqual(actual, False)

if __name__ == '__main__':
    unittest.main()
        
