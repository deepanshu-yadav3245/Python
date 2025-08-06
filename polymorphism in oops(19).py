# POLYMORPHISM:- polymorphism means function name (but different signatures) being uses for different types.

l = [10, 20, 30, 40.50]
print(len(l))         # polymorphism ekk chiz ke multiple form hote hai
s = "welcome rahul"
print(len(s))

print()


class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(12,45)
num1.showNumber()

num2 = Complex(4,7)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()




# method  and of overloading:---

# it is worked in the same method names and difficult arguments.
# Argument different will be based on a number of argument and type of arguments.

def find_area(x=None, y=None):

    if x != None and y != None:
        print(x * y)
    elif x != None:
        print(x * x)
    else:
        print("Nothing")


class Area:
    pass


obj1 = Area()
find_area()
find_area(12)
find_area(10,20)


# Method of overriding:--

# method overriding is the method having the same name with the same arguments
# it is implemented with inheritance also.  it mostly used for memory reducing processes.

class A:
    def showdata(self):
        print("I am in A class")

class B(A):
    def showdata(self):
        print("I am in B class")

obj = B()
obj.showdata()