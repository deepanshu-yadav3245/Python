# (1):-  WHAT IS A LIST  COMPREHENSION:- It is a way of writing compact code in python. example:-
from typing import List

# list[]
# for i in range (1,4)
#        for j in range(5,7)  # this is a long term we can use list comprehension to execute the code in one line.below
#        list.append(i*j)
# print(l)

# print([i*j for j in range(5,7) for i in range(1,4)])

# TYPE OF LIST COMPREHENSION:- (1)LIST COMP,     (2)SET COMP,    (3)DICTIONARY COMP

# syntax(1):- [expression for variable in iterable]
nums = [3, 6, 8, 12, 14, 15]
sq = []
for num in nums:
    sq.append(num * num)
print(sq)

# Using list comprehension
print([num * num for num in nums])

print()

# syntax(2):- [expression for variable in iterable if- condition]
nums = [3, 6, 8, 12, 14, 15]
sq = []
for num in nums:
    if num % 2 == 0:
        sq.append(num * num)
print(sq)

# Using List comprehension
print([num * num for num in nums if num % 2 == 0])

print()

# syntax(3):- [expression for variable in iterable nested if condition]
nums = [3, 6, 8, 12, 14, 15]
sq = []
for num in nums:
    if num % 2 == 0:
        if num % 3 == 0:
            sq.append(num * num)
print(sq)

# Using List comprehension
print([num * num for num in nums if num % 2 == 0 if num % 3 == 0])

print()

# syntax(4):- [expression if cond else expression for variable in iterable]
nums = [3, 6, 8, 12, 14, 15]
result = []
for num in nums:
    if num % 2 == 0:
        result.append(num * num)
    else:
        result.append(num * num * num)

print(result)

# Using List comprehension
print([num * num if num % 2 == 0 else num * num * num for num in nums])

print()

# syntax(4):- [expression if cond else expression for variable in iterable]
nums = [3, 6, 8, 12, 14, 15]
result = []
for num in nums:
    if num % 2 == 0:
        result.append(num * num)
    else:
        result.append(num * num * num)

print(result)

# Using List comprehension
print([num * num if num % 2 == 0 else num * num * num for num in nums])

print()

# syntax(5):- [expression if cond else expression for variable in iterable]
list = []
for i in range(3, 6):
    for j in range(5, 7):
        list.append(i * j)
print(list)
# Using List Comprehension
print([i * j for i in range(3, 6) for j in range(5, 7)])

# ADVANTAGE OF LIST COMPREHENSION:
# (1):- Compact and Elegent code , (2):- less code ,(3):- faster execution








