# RANDOM MODULE

# (1) PYTHON RANDOM RANDINT()METHOD

# Return a number between 5 and 10(both include):
# Import random
# print(random.randint(5,10))

# (1.1) Return a number between 3(include) and 9(not include)
# print(random.randrange(3,9))

#  (2) PYTHON RANDOM CHOICE()METHOD

# Return a random element from a list:
# l["apple","banana","cherry"]
# print(random.choice())

import random

n = random.randint(2, 8)
print(n)


print()


n1 = random.randrange(2, 4)
print(n1)


print()


l = [10, 20, 30, 40]
lc = random.choice(l)
print(lc)


print()


r = random.random()  # Return a random float number between 0 and 1
print(r)

print()

l = [40, 50, 60, 70, 80, 90]  # Take a sequence and return the sequence in a random order.
random.shuffle(l)
print(l)

print()
3

u = random.uniform(3, 9)  # Return a random float  number between two given parameter
print(u)