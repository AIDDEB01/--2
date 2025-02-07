
class Shape:
    def __init__(self):
        self.area = 0


class Square(Shape):
    def __init__(self):
        self.num = 0
        super().__init__()
        self.lenth = 0

    def getLenth(self):
        self.lenth = int(input("Lenth:"))

    def getArea(self):
        self.num = self.lenth*self.lenth
        print(f"Area: {self.num}")

class Rectangle(Shape):

    def __init__(self):
        super().__init__()


        self.width = 0
        self.lenth = 0

    def getNum(self):
        self.width = int(input("Width:"))
        self.lenth = int(input("Lenth:"))
    def getArea(self):
        self.area = self.lenth * self.width
        print(f"Area:{self.area}")

obj = Rectangle()
obj.getNum()
obj.getArea()

