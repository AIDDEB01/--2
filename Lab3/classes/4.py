import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Show(self):
        print(f"Point({self.x}:{self.y})")
    def Move(self,x,y):
        self.x = x
        self.y = y
    def Distance(self,other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        print(f"Distance:{distance}")


a = int(input())
a1 = int(input())
b = int(input())
b1 = int(input())

p = Point(a,b)
p.Show()
p.Move(0,2)
p.Show()

p2= Point(a1,b1)

p.Distance(p2)
