class DemoClass:
    a = 12

    def __init__(self):
        print("welcome to wscubetech")  # def init is used for construction in oops

    def showvalue(self):
        self.c = self.a * self.a
        print(self.c)

    def showvalue1(self, a, b):
        print(a + b)


obj = DemoClass()
obj.showvalue()
obj.showvalue1(102, 345)
