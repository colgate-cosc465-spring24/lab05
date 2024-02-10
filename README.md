# Lab 05: Internet Protocol (IP) subnets

## Overview
In this lab, you will implement two functions for analyzing Internet Protocol (IP) subnets. 

### Learning objectives
After completing this lab, you should be able to:
* Compute whether a network is a subnet or supernet of another network
* Write functions that mask and compare IP addresses

## Getting started
Clone your git repository on a tigers servers.

As you work on this lab, you should refer to the [documentation for the ipaddress](https://docs.python.org/3.8/library/ipaddress.html) Python library. Make sure you consult the documentation for the Python 3.8 version of this library, which is the version installed on the tigers servers; older/newer versions of this library have different capabilities. Also, you may want to refer to the recommended reading [Understanding IP Addresses, Subnets, and CIDR Notation for Networking](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking) and/or use a [subnet calculator](http://www.subnet-calculator.com/cidr.php) to help you better understand how network addresses are related.

## Part 1: `is_subnet`

Your first task is to write the `is_subnet` function (in `ipsubnet.py`). The function takes two networks—`supernet` and `subnet`—and should return `True` if `subnet` is a subnetwork of `supernet`. 

You can assume the parameters will be <code>[IPv4Network](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Network)</code> or <code>[IPv6Network](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv6Network)</code> objects. Your function **may not** use the <code>[subnets](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Network.subnets)</code>, <code>[supernet](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Network.supernet)</code>, <code>[subnet_of](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Network.subnet_of)</code>, or <code>[supernet_of](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Network.supernet_of)</code> methods from these classes.

Note that Python has standard bitwise operators (`&`, `|`, `~`, `<<`, `>>`) just like C and Java. You can apply these operators to an integer representation of an <code>[IPv4Address](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Address)</code> or <code>[IPv6Address](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv6Address)</code>, which you can get by casting one of these objects to an integer: 
```Python
addr = int(IPv4Address('10.11.12.13'))
```

Since a subnet is defined in terms of a prefix (or network address) and a prefix length (or network mask), you cannot convert a network object (<code>[IPv4Network](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Network)</code> or <code>[IPv6Network](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv6Network)</code>) to an integer. However, you can convert a network prefix to an integer, for example:
```Python
addr = int(IPv4Network('10.0.0.0/8').network_address)
```

You can test your functions by running `test_is_subnet.py`, which contains 7 unit tests. You are also welcome (but not required) to add your own unit tests to this file.

## Part 2: `is_adjacent`

Your second task is to write the `is_adjacent` function (in `ipsubnet.py`). The function takes two subnets—`netA` and `netB`—and should return `True` if the range of addresses contained in `netA` immediately precedes or follows the range of addresses contained in `netB`. For example, the subnet `192.168.0.0/24` covers the range of addresses `192.168.0.0` through `192.168.0.255` and the subnet `192.168.1.0/24` covers the range of addresses `192.168.1.0` through `192.168.1.255`, so these two subnets are adjacent. In contrast, the range of addresses covered by 192.168.1.128/25 starts at `192.168.1.128`, so `192.168.1.128/25` is not adjacent to `192.168.0.0/24`. 

You can assume the parameters will be <code>[IPv4Network](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv4Network)</code> or <code>[IPv6Network](https://docs.python.org/3.8/library/ipaddress.html#ipaddress.IPv6Network)</code> objects. You may use any methods from these classes.

You can test your functions by running `test_is_adjacent.py`, which contains 8 unit tests. You are also welcome (but not required) to add your own unit tests to this file.

## Self-assessment
The self-assessment for this lab will be available on Moodle after 5pm on Thursday, February 22. Please complete the self-assessment by 11pm on Monday, February 26.