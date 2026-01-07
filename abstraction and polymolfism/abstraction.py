# Abstract Base Class

class Shape():

    def __init__(self, shapeType):

        '''Initializes the Shape with a type (e.g., Rectangle, Circle)'''

        self.shapeType = shapeType


    def area(self):

        '''Abstract method to compute the area. To be implemented by subclasses.'''

        pass


    def perimeter(self):

    '''Abstract method to compute the perimeter. To be implemented by subclasses.'''

        pass


# Rectangle class implementing Shape

class Rectangle(Shape):

    def __init__(self, length, breadth):

        '''Initializes Rectangle with length and breadth'''

        super().__init__('Rectangle')

        self.length = length

        self.breadth = breadth


    def area(self):

       '''Computes the area of the Rectangle'''

        return self.length * self.breadth


    def perimeter(self):

        '''Computes the perimeter of the Rectangle'''

        return 2 * (self.length + self.breadth)


# Circle class implementing Shape

class Circle(Shape):

pi = 3.14


    def __init__(self, radius):

        '''Initializes Circle with radius'''

        super().__init__('Circle')

        self.radius = radius


    def area(self):

        '''Computes the area of the Circle'''

        return round(Circle.pi * (self.radius ** 2), 2)


    def perimeter(self):

        '''Computes the perimeter of the Circle'''

        return round(2 * Circle.pi * self.radius, 2)


# Creating a Rectangle object with length 30 and breadth 15

rectangle = Rectangle(30, 15)

print("Area of Rectangle: ", rectangle.area()) # 450

print("Perimeter of Rectangle: ", rectangle.perimeter()) # 90

# Creating a Circle object with radius 5

circle = Circle(5)

print("Area of Circle: " , circle.area()) # 78.5

print("Perimeter of Circle: ", circle.perimeter()) # 3