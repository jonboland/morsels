import math

class Circle:
    
    """Class to represent a circle."""
    
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Circle dimensions cannot be negative")
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2  

    @property
    def area(self):
        return self.radius**2 * math.pi
