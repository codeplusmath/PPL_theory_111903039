import turtle

s = turtle.getscreen()
t = turtle.Turtle()


class shape:
    def __init__(self, length=0, sides=0):
        self.length = length
        self.sides = sides

    def perimeter(self):
        return self.length*self.sides


class polygon(shape):
    def info(self):
        print("A polygon can be defined as a flat or plane, two-dimensional  with straight sides.")


class square(polygon):
    name = "square"

    def __init__(self, length):
        self.length = length
        self.sides = 4

    def area(self):
        return self.length**2

    def show(self):
        for _ in range(self.sides):
            t.forward(self.length)
            t.right(90)


class pentagon(polygon):
    name = "pentagon"

    def __init__(self, length):
        self.length = length
        self.sides = 4

    def area(self):
        return (self.length**2)*1.72

    def show(self):
        for _ in range(self.sides):
            t.forward(self.length)
            t.right(72)


class hexagon(polygon):
    name = "hexagon"

    def __init__(self, length):
        self.length = length
        self.sides = 6

    def area(self):
        return (self.length**2)*2.598

    def show(self):
        for _ in range(6):
            t.forward(self.length)
            t.right(60)


class octagon(polygon):
    name = "octagon"

    def __init__(self, length):
        self.length = length
        self.sides = 8

    def area(self):
        return (self.length**2)*4.83

    def show(self):
        for _ in range(8):
            t.forward(self.length)
            t.right(45)


class triangle(polygon):
    name = "triangle"

    def __init__(self, length):
        self.length = length
        self.sides = 4

    def area(self):
        return (self.length**2)*0.43

    def show(self):
        for _ in range(3):
            t.forward(self.length)
            t.left(120)


hex1 = hexagon(100)
oct1 = octagon(100)
pent1 = pentagon(100)
shapes = [pent1, hex1, oct1]
# to demonstrate virtual function, area
for shape in shapes:
    print("Area of ", shape.name, "is", shape.area())
hex1.show()
turtle.done()
