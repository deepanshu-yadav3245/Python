# How to create lambda function:---

add = lambda a: a + 4555
print(add)
print(add(20))

print()

sum = lambda a, b: (a + b, a - b)
add, sub = sum(10, 90)
print(add)
print(sub)

print()

#you can pass any type of argument:--


sum = lambda a, b=200: (a + b, a - b)
add, sub = sum(a=100)
print(add)
print(sub)

# WHY LAMBDA FUNCTION:--

#  USED AS FUNCTION ARGUMENTS
#  MEMORY EFFICIENT
#  FAST EXECUTION
#  CAN BE USED WITH FILTER(),MAP(),REDUCE() FUNCTIONS.


print()

# nested lambda function:--

add = lambda x: lambda y: (x + y)

func = add(10)

print(func(30))

print()

square = lambda n: n ** 2


def modify(func):
    num = int(input("Enter a number:"))
    return func(num) + num


print(modify(square))

print()

# Lambda function with if else & List comprehension:-----

# (1):- short hand if else

num1 = 20
num2 = 30

if num1 >= num2:
    print(num1)
else:
    print(num2)

print(20 if num1 >= num2 else 30)  # short hand if - else

print()

# python Lambda function with if-else:--

num1 = 39
num2 = 19

max1 = lambda n1, n2: n1 if n1 >= n2 else n2
print(max1(num1, num2))

print()

# Using List comprehension with lambda function:---

nums = [3, 5, 6, 7]
square = lambda data: [i * i for i in nums]
print(square(nums))
