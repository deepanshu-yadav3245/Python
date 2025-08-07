# DECORATOR:
# Function which takes other function as input,add additional functionalities and return it.
# It is a callable python which modifies other functions/class.


def decor(func):
    def inner():
        func()  # existing functionality
        # addd new functionality
        print("welcome!")

    return inner


@decor
def printer():
    print("welcome!")
    print("welcome!")


printer()


# example

def decor(addition):
    def inner():
        result = addition()  # existing functionality
        # add new functionality here
        num3 = float(input("Enter the third number"))
        result = result + num3
        return result

    return inner


@decor
def addition():
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    result = num1 + num2
    return result


print("addition is:", addition())

