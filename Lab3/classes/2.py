
class Shape:
    def __init__(self):
        self.num = 0


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


obj = Square()
obj.getLenth()
obj.getArea()

