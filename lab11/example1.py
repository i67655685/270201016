import math
# I cant run my code exactly how I want
class Cylinder:  
    def __init__(self, radius, height):
        self.radius = (self, radius)
        self.height = height

    def get_surface(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius**2

    def get_volume(self):
        return math.pi * self.radius**2 * self.height
def main():
    cyl = Cylinder(3, 5) 
    print('Cylinder area:', cyl.get_surface()) 
    print('Cylinder volume:', cyl.get_volume())