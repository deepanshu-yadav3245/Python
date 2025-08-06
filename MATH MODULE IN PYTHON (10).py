# MATH.CEIL(X)

# Return the ceiling of X the smallest integer greater than or equal to x. if x is not a float delegates to x.__ceil__()
#  which should return an integer an integral value.
# x=10.5
# print(math.ceil (x) #output 11

import math

x = 12.2
print(math.ceil(x))

# MATH.FABS(X)

# Return the absolute value of x.
# x=-10
# print(math.fabs(x)
# output 10

import math

x = -20
print(math.fabs(x))

# MATH FACTORIAL(X)

# Return x factorial as integer.Raise value error if x is not integer or is negative.
# x=5
# print(math.factorial(x))
# output=120

import math

x = 2
print(math.factorial(x))

# MATH.FLOOR(X)

# Return the floor of x,largest integer less than equal to x.if x is not a float,delegate to x__floor__(),
# which should return an integer values
# x=10.5
# print(math.floor(x)) output: 10

import math

x = 10.9
print(math.floor(x))

# MATH.FSUM(ITERABLE)

# Return an accurate floating point sum of values in the iterable.

import math

l = [10, 20, 30, 40]
print(math.fsum(l))

# MATH.SQRT(X) ,Return the square root of x

print(math.sqrt(144,))


