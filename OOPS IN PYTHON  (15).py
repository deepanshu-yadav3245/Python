class Car:
    color = "blue"
    brand = "mercedes"


car1 = Car()
print(car1.color)
print(car1.brand)

print()


# __init__function:--

class Student:
    name = "rahul"

    def __init__(self, fullname,
                 marks):  # self:-- the self parameter is a reference to the current instance of the class,and is used to access variable that belong to class.
        self.name = fullname
        self.marks = marks
        print("adding new student  in Database...")


s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("rahul", 88)
print(s2.name, s2.marks)
print()


# create student class that takes name & marks of 3 subject as argument in constructor.create a method print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
      sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "your avg score is:", sum / 3)


s1 = Student("rahul yadav", [99, 98, 97])
s1.get_avg()
