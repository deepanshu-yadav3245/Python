# Iterator:-- An iterator is an object that allows programmer to travers through a sequence of data without storing the
#             data in the memory.

# Iteration:- Process of taking each item of something one after another
# Iterable:- jiske upper iteration hota hai .this is container multiple items
#  every iterator is iterable. you can run loop on very iterator.

# How to create iterator.

l = [10, 20, 30, 40, 50, 60, ]  # iterable but not iterator

iter_obj = iter(l)

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

# or we can also use for loop:

for element in iter_obj:
    print(element)

print()

# using magic method directly:
L = [10, 20, 30, 40]  # iterable

iter_obj = L.__iter__()  # iterator
print(type(iter_obj))

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())

print()

# Program for checking iterator or iterable:-

object1 = iter(eval(input("Enter object")))
object_dir = dir(object1)
if '__iter__' in object_dir and '__next__' in object_dir:
    print("Iterator operation goes here")
elif '__iter__' in object_dir:
    print("Iterable operation goes her")
else:
    print("not supported")


# type of iterator:- 1- built-in iterator(runs internally) ex.iterator of range()function
#                    2- Custom iterators

# How to create a custom iterator.
class PowerOfTwo:
    def __init__(self, max_value):
        self.limit = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:  #32<=16
            result = self.current
            self.current = self.current * 2
            return result
        else:
            raise StopIteration


n = int(input("Enter the limit"))
iter_obj = PowerOfTwo(n)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))


# own range() function
class my_range:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return my_range_iterator(self)


class my_range_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj = iterable_obj

    def __iter__(self):
        return self


    def __next__(self):
        if self.iterable_obj.start <= self.iterable_obj.stop:
            result = self.iterable_obj.start
            self.iterable_obj.start = self.iterable_obj.start + self.iterable_obj.start
            return result
        else:
            raise StopIteration

a = my_range(2,10,3)
iter_obj = iter(a)
print(next(iter_obj))
print(next(iter_obj))












