# ZIP FUNCTION

l = [10, 20, 30, 40]
l1 = [3, 4, 77, 88, 23]

t = len(l)

for a, b in zip(l, l1):
    print(a, b)

    print()

for h in range(t):
    print(l[h], l1[h])
