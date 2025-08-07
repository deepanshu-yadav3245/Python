# WHAT IS GENERATORS:--
# In python ,a generator is a function that return an iterator that produce a sequence of value when iterated over.
# Generator are useful when we want to produce large sequence of values,but we don't want to store all of them in memory


#  CREATE PYTHON GENERATOR:--
# In python,similar to defining a normal function using the (def) keyword,but instead of the (return) statement we use
# the (yield) statement. Here,the (yield) keyboard is used to produce a value from the generator:--


# USE OF GENERATORS:--
# (1) Easy to Implement, (2) Memory Efficient, (3) Represent Infinite Stream, (4) Pipelining Generator


# CREATING A GENERATOR FUNCTION:--
def my_gen():
    yield "hello world"
    yield "i am rahul"
    yield "coder"


g = my_gen()
print(next(g))
print(next(g))
print(next(g))
print(type(g))

print()


def countdown(num):
    print("countdown starting...")
    while num > 0:
        yield num
        num = num - 1


g = countdown(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

