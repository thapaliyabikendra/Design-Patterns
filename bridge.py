class DrawingAPIOne:
    """Abstraction: concrete class 1"""

    def draw_circle(self, x, y, radius):
        print(f"API 1 drawing a circle at ({x}, {y} with radius {radius}!)")

class DrawingAPITwo:
    """Abstraction: concrete class 2"""

    def draw_circle(self, x, y, radius):
        print(f"API 2 drawing a circle at ({x}, {y} with radius {radius}!)")

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)
    
    def scale(self, percent):
        """Implementation independent"""
        self._radius *= percent

circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

circle2 = Circle(1, 2, 3, DrawingAPITwo())
circle2.scale(10)
circle2.draw()