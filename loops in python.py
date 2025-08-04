from typing import List

range(5)
# start=0
# condition<5
# increment 1
# 0 1 2 3 4

range(1, 6)
# start=1
# condition<5
# increment 1
# 1 2 3 4 5

range(1, 6, 2)
# start=1
# condition<6
# increment 2
# 1 3 5

for n in range(5):
    print(" rahul")

print()

for n in range(1, 6):
    print(n)

print()

for n in range(1, 6, 2):
    print(n)

# print the table of 2
for a in range(1, 11):
    print("2 *", a, "=", 2 * a)

    print()

# range in reverse

# range(10,0,-1)

for n in range(10, 0, -1):
    print(n)

print()  # this is use for space in output
# print the first 10 natural number using loop

n = 11
for i in range(1, n):
    print(i)

# python program to print all the even number within the given range.

print()  # this is use for space in output
n = 100
for i in range(1, n):
    if i % 2 == 0:
        print(i)
print() # this is use for space in output

# python program to convert the month to a number of days.



