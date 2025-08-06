# How to create your own module in python

#module1.py
def sum(a, b):
    c = a + b
    return c


def mul(a, b):
    c = a * b
    return c


#checking.py
import module1

print(module1.sum(10, 20))

import module1 as m

print(m.sum(10, 20))
print(m.mul(10, 20))

from module1 import *

print(sum(10, 20))
print(mul(10, 20))
