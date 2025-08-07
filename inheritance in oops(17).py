# INHERITANCE:---
# When one class (child/derived) derives the properties & method of another class(parent/base)
class A:
def displayA(self):
    print("welcome to wscubetech A")

class B(A):
    def displayB(self):
        print("welcome to wscubetech B")


class C(B):
    def displayC(self):
        print("welcome to wscubetech C")  # multilevel inheritance


obj = C()
displayA()
obj.displayB()
obj.displayC()


# PROPERTY FUNCTION :-- we use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

        @property
        def percentage(self):
            return str((self.phy + self.chem + self.math) / 3) + "%"

    stu1 = Student(98,99,99)
    print(stu1.percentage)

    stu1.phy = 86
    print(stu1.peercantage)
