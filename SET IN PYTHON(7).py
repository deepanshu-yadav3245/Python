# SET IN PYTHON


# A set is a collection which is unordered and unindexed that is iterable,mutable,and has no duplicate elements.
# In python sets are written with curly brackets.

# set(),add(),pop(),remove(),clear(),discard(),updated(). these are the  function used in set
# remove:- if the item to remove does not exit,remove ()will raise an error
# Discard:- if the item to remove does not exit, discard ()will NOT raise an error
s = [10, 20, 30, 40]
print(s)

for a in s:
    print(a)  # set iterate karte  hai

print()

l = [10, 20, 30, 40]
s = set(l)
print(s)  # set() function

print()

s = {10, 20, 30, 40, 50, }
s.remove(20)
print(s)  # remove() function

print()

d = {30, 40, 60, 50, 70}
d.discard(40)
print(d)  # discard() function

print()

p = {20, 30, 56, 70, 50}
print(s.pop())
print(p)  # pop() function

p.clear()
print(p)  # clear() function

p.add(3)
print(p)  # add() function

l = [20, 40, 50, 30, 70]
s = {2, 4, 5, 7, 8, }
s.update(l)
print(s)  # update() function
