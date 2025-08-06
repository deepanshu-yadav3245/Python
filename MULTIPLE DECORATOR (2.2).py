def decor1(func):
    def inner():
        return func().upper()

    return inner


def decor2(func):
    def inner():
        return func().split()

    return inner


@decor2
@decor1
def get_name():
    name = input("Enter first name:--")
    sirname = input("Enter the sirname:--")
    full_name = name + " " + sirname
    return full_name


print(get_name())


# one decorator on multiple functions:--
def decor(func):
    def inner(*args):
     for num in args[1:]:
        if num == 0:
            return "cannot divide by zero"
        return func(*args)
    return inner


@decor
def div1(a, b):
    return a / b


@decor
def div2(a,b,c):
    return a/b/c


print(div1(10,5))
print(div1(10,0))
print(div2(10,0,5))
print(div2(10,20,0))
print(div2(0,10,5))