#!/usr/bin/python3

import ipaddress
import ipsubnet
import unittest

class TestAggregate(unittest.TestCase):
    def test_aggregate_subnet_same_prefix(self):
        actual = ipsubnet.aggregate(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('10.0.0.0/16'))
        self.assertEqual(actual, ipaddress.IPv4Network('10.0.0.0/8'))

    def test_aggregate_subnet_diff_prefix(self):
        actual = ipsubnet.aggregate(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('10.128.0.0/16'))
        self.assertEqual(actual, ipaddress.IPv4Network('10.0.0.0/8'))

    def test_aggregate_adjacent_same_prefixlen_even(self):
        actual = ipsubnet.aggregate(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.0.0.0/8'))
        self.assertEqual(actual, ipaddress.IPv4Network('10.0.0.0/7'))

    def test_aggregate_adjacent_same_prefixlen_odd(self):
        actual = ipsubnet.aggregate(ipaddress.IPv4Network('9.0.0.0/8'),
                ipaddress.IPv4Network('10.0.0.0/8'))
        self.assertEqual(actual, None)

    def test_aggregate_adjacent_diff_prefixlen(self):
        actual = ipsubnet.aggregate(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('11.0.0.0/16'))
        self.assertEqual(actual, None)

    def test_aggregate_none(self):
        actual = ipsubnet.aggregate(ipaddress.IPv4Network('10.0.0.0/8'),
                ipaddress.IPv4Network('12.0.0.0/8'))
        self.assertEqual(actual, None)

if __name__ == '__main__':
    unittest.main()
        
