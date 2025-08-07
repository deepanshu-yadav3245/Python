# SHORT HAND WAY TO CREATE GENERATOR:--

# write a python program for finding squares of first n numbers
import sys

n = 5
L = (i * i for i in range(1, n))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(type(L))
print(sys.getsizeof(L))

print()


# WHAT IS FIBONACCI SERIES:- The fibonacci series is a mathematical sequence that start with 0 and 1, with e
#                            subsequent number being the sum of the two preceding ones.( ex:- 0 1 1 2 3 5 8 13 21 34 55..)


# PYTHON PROGRAM FOR FIBONACCI SERIES USING GENERATOR:
def fibo():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


g = fibo()
# print(next(g))
# print(next(g))
# print(next(g))  0r  we use for loop niche dekh bsdk
# print(next(g))
# print(next(g))
# print(next(g))
for i in g:
    if i >= 1000:
        break
    print(i)

print()


# CHAINING GENERATOR IN PYTHON:--

# ''' Suppose you have a list of numbers,and you want to filter out even no square the filtered even no and add them up.
def filter_even(seq):
    for num in seq:
        if num % 2 == 0:
            yield num


def find_squares(seq):
    for num in seq:
        yield num * num


def summation(seq):
    total = 0
    for num in seq:
        total = total + num
        yield total


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
g = summation(find_squares(filter_even(numbers))) # This is called chaining generator
print(next(g))

# g = filter_even(numbers)
# g1 = find_squares(g)
# g2 = summation(g1)

# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
