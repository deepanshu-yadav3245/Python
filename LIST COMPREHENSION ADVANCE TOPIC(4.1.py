# How To  Use  'IF-ELIF-ELSE'  In List Comprehension:-

# if-elif-else

# if cond1:
#  code1
# elif cond2:
#   code2
# elif cond3:
#   code3
# else:
#   code4

# chaining condition:-
# code1 if code1 else code2 if code2 else code3 if code3 else code4

# EXAMPLE (1)
num = int(input("Enter a number"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Using Chaining
print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

print()

# if-elif-else in list comprehension
nums = [90, 0, -35, -99, 98, -89]
status = []
for num in nums:
    if num > 0:
        status.append("Positive")
    elif num < 0:
        status.append("Negative")
    else:
        status.append("Zero")
print(status)

# Using chaining
print(["Positive" if num > 0 else "Negative" if num < 0 else "Zero" for num in nums])

print()

# (2):--DICTIONARY COMPREHENSION:-
# syntax:- {key: value for (key,value) in iterable}       Use {} bracket

nums = [1, 4, 5, 6, 8, 10]
my_dict = {}
for num in nums:
    if num % 2 == 0:
        my_dict[num] = num ** 2
print(my_dict)
print(type(my_dict))
# Using dictionary
print({num: num ** 2 for num in nums if num % 2 == 0})

print()

str1 = "cOding"
my_dict = {}
for char in str1:
    my_dict[char.upper()] = (ord(char), ord(char.swapcase()))

print(my_dict)

# using Dictionary
print({char.upper(): (ord(char), ord(char.swapcase())) for char in str1})


print()

# (3):-SET COMPREHENSION:- set is a unordered data structure use {} bracket

nums = [1, 2, 3, 4, 5, 5, 6]
print({n ** 2 for n in nums})

# notes:- new data structure  with new element tabhi comprehension ka use karte hai
