# integer
# float
# complex numbers

# a=5  print(a,"is of type", type(a)) #5 is of type<class int>
# a=2.0 print(a,"is of type",type(a)) #2.0 is type<class of float >
# number kabhi bhi cotation mai nhi likha jayega.

a = 24
print(a, type(a))

b = 23.8
print(b, type(b))

c = 2 + 5j
print(c, type(c))

# STRING
# A string is a collection of one or more characters put in a single quote,double quote or triple quote
# multi line string can be denoted using triple quotes,

s = "hello"
print(s, type(s))

s = '''hello rahul'''
print(s,type(s))

# LIST

# list is ordered sequence of item
#  it is one of the most used datatype in python and is very flexible
# [] example , a=[1,2,3,4]

l = [1, 2, 3, 4]
print(l, type(l))
l[3] = 29
print(l, type(l))

# TUPLE

# tuple is an ordered sequence of item same as a list
# it is  defined within parentheses () where item are separated by commas example,t=(5,'program',1+3j)

t = (12, 23, 'Hello')
print(t, type(t))

# DICTIONARY

# dictionary is an unordered collection of key value pairs.
# in python,dictionaries are defined within braces{} with each item begin a pair in the form key:value
# example d={1:'value','key':2}
# print(type(d)) , mutabale data type


d = {
    'course_name': 'python',
    'course_duration': '2 month'
}
print(d, type(d))

print(d['course_name'])
print(d['course_duration'])

# SET

# A set is unordered collection of items
# every set element is unique (no duplicate ) and must be immutable (cannot be changed)
# {}     EXAMPLE= my_set={1,2,3,4}
#                print(my_set)

s = {10, 12, 20, 34, 20}
print(s, type(s))
